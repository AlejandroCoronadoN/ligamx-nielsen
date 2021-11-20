import pandas as pd 
import numpy as np 
from tqdm import  tqdm
from dict_2015 import dict_2015
from dict_2016 import dict_2016
from dict_2017 import dict_2017
from dict_2018 import dict_2018
from dict_2019 import dict_2019
from dict_2020 import dict_2020

unique_demographic_groups = ['Hombre', 'Mujer', 'Milenials', 'No milenials', '18-25', '26-35',
       '36-45', '46-55', '56+', 'AB', 'C+', 'C', 'C-', 'D+/D/E',
       'Aguascalientes', 'Cancún', 'CDMX', 'Celaya', 'Ciudad Juárez',
       'Ciudad Victoria', 'Culiacán', 'Guadalajara', 'Hermosillo', 'León',
       'Mazatlán', 'Mérida', 'Morelia', 'Monterrey', 'Oaxaca', 'Pachuca',
       'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tepatitlán',
       'Tijuana', 'Tlaxcala', 'Toluca', 'Torreón', 'Villa Hermosa',
       'Zacatecas', 'Resto', 'América', 'Atlas', 'Chivas', 'Cruz Azul',
       'Pumas', 'Tigres', 'Rayados', 'Santos', 'Mazatlán FC', 'Necaxa',
       'FC Juárez', 'Atlético San Luis', 'Alebrijes', 'Atlante',
       'Cancún FC', 'Cimarrones de Sonora FC', 'Club Celaya',
       'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco',
       'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico Madero FC',
       'U de G', 'Venados FC', 'Ninguno', 'Heavy', 'Medium', 'Light',
       'Fan base 1', 'Fan base 2', 'Fan base 3', 'Liga MX', 'Ascenso MX',
       'Liga MX and Ascenso MX', 'No practica', 'Si practica',
       'A veces practiva', 'Practica frecuente', True, False,
       'Tarjeta de débito', 'Tarjeta de crédito', 'Banco en línea',
       'Clientes BBVA Bancomer', 'Otros Bancos', 'CONOCE', 'USA']
       
xls = pd.ExcelFile('data/Ola_6_2020.xlsx')
sheet_names = xls.sheet_names
sheet_dict = dict_2020
df_year = pd.DataFrame()
for sheet  in tqdm(sheet_names):
    if sheet not in ['Contents', 'MUESTRA', 'Q1B', 'Q2BEDAD']:
        df_answ = pd.read_excel(xls, sheet_name=sheet, skiprows = sheet_dict['answers']['skiprows'], usecols = sheet_dict['answers']['usecols'])
        question = pd.read_excel(xls, sheet_name=sheet, skiprows = sheet_dict['question']['skiprows'], usecols = sheet_dict['question']['usecols']).columns[0]
        print(f'Starting year = {2020} \nquestion {question} ')
        #Rename the column
        df_answ.columns = [question]
        #We just want to include the answer to the question not the statistical values
        for cutword  in sheet_dict['answers']['cutwords']:
            df_cut = df_answ[ df_answ[question].replace(np.nan, '').str.startswith(cutword).replace(np.nan, False) ]
            if len(df_cut)>0:
                cutindex = df_cut.index[0]
                break
        #We cut the df at the cutword index position
        df_answ = df_answ[:cutindex]
        #We only want the values asociated with the anwers not the statistical values
        df_answ = df_answ.dropna()
        valuesindex = df_answ.index

        df_question = pd.DataFrame()
        print(f'\n\n--------------------\nStarting year = {2020} \nquestion {question} \n df_question.shape: {df_question.shape}')

        for demographic in tqdm(sheet_dict.keys()):
            if demographic in ['question', 'answers', 'questions_list']:
                continue
            else:
                df = pd.read_excel(xls, sheet_name=sheet, skiprows = sheet_dict[demographic]['skiprows'], usecols = sheet_dict[demographic]['usecols'])
                df = df.loc[valuesindex]
                df.columns = sheet_dict[demographic]['columns']
                df = df_answ.join(df)
                #df[question] = df[question].apply(lambda x: str(question)  + ' - ' + str(x))
                df['question'] =  question
                #df = df.set_index(question)
                #df 
                #df_t = df.transpose()
                #df_t = df_t.reset_index()
                df = df.rename(columns ={question:'answer_group'})
                df['demographic'] = demographic
                df = df.melt(id_vars =['demographic', 'question', 'answer_group'])
                df = df.rename(columns ={'variable':'demographic_group'})
                
                #Testying atypical or new values in demographic variables
                atypical_demogrpahic_values = [x for x in df.demographic_group.unique() if x not in unique_demographic_groups]
                if len(atypical_demogrpahic_values) >0:
                    raise ValueError()
                else:
                    #Non empty df_qestion
                    if len(df_question) == 0:
                        df_question = df
                    else:
                        df_question = df_question.append(df)
                        #print(f'\tdf_question.shape: {df_question.shape}')
                
        if len(df_year) == 0:
            df_year = df_question
        else:
            df_year = df_year.append(df_question)
            
import pandas as pd 
import numpy as np 
from tqdm import  tqdm

xls = pd.ExcelFile('data/Ola_6_2020.xlsx')
sheet_names = xls.sheet_names

xls_dict = {
    
    
    2020:{
        'questions_list': [], 
        'answers': {
            'skiprows' : 8, 
            'usecols':'B:B',
            'cutwords': ['Columns Tested', 'Media']
        },
        
        'question': {
            'skiprows' : 2, 
            'usecols':'B:B'
        },
        
        'sexo':{
            'skiprows' : 8, 
            'usecols':'D:E',
            'columns': ['Hombre',	'Mujer']
        },
        
        'generacion':{
            'skiprows' : 8, 
            'usecols':'F:G',
            'columns': ['Milenials', 	'No milenials']
        },
        
        'edad':{
            'skiprows' : 8, 
            'usecols':'H:L',
            'columns': ['18-25',	'26-35',  '36-45', 	'46-55', 	'56+']
        },
        
        'NSE':{
            'skiprows' : 8, 
            'usecols':'M:Q',
            'columns': ['AB', 	'C+', 'C', 'C-', 'D+/D/E']
        }, 

        'Ciudad':{
            'skiprows' : 8, 
            'usecols':'R:AS',
            'columns': ['Aguascalientes', 'Cancun', 'CDMX', 'Celaya', 'Ciudad Juarez', 'Ciudad Victoria', 'Culiacan', 'GDL', 'Hermosillo', 'Leon', 'Mazatlan', 'Merida', 'Morelia', 'MTY', 'Oaxaca', 'Pachuca', 'Puebla', 'Queretaro', 'San Luis Potosí', 'Tampico', 'Tepatitlán', 'Tijuana', 'Tlaxcala', 'Toluca', 'Torreon (Laguna)', 'Villa Hermosa', 'Zacatecas', 'Resto']
        },

        'Equipo Favorito':{
            'skiprows' : 8, 
            'usecols':'AT:CB',
            'columns': ['América', 'Atlas', 'Chivas(Guadalajara)', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados (Monterrey)', 'Santos', 'Toluca', 'León', 'Tijuana', 'Mazatlán FC', 'Puebla', 'Pachuca', 'Querétaro', 'Necaxa', 'FC Juárez', 'Atlético San Luis', 'Alebrijes de Oaxaca', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Club Atlético Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico M Fútbol Club', 'U DE G', 'Venados FC', 'Ninguno']
        },
        
        'Segundo Equipo':{
            'skiprows' : 8, 
            'usecols':'CC:DK',
            'columns': ['América', 'Atlas', 'Chivas(Guadalajara)', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados (Monterrey)', 'Santos', 'Toluca', 'León', 'Tijuana', 'Mazatlán FC', 'Puebla', 'Pachuca', 'Querétaro', 'Necaxa', 'FC Juárez', 'Atlético San Luis', 'Alebrijes de Oaxaca', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Club Atlético Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico M Fútbol Club', 'U DE G', 'Venados FC', 'Ninguno']
        },
        
        'Equipo Segunda':{
            'skiprows' : 8, 
            'usecols':'DL:EB',
            'columns': ['Alebrijes de Oaxaca', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Club Atlético Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico M Fútbol Club', 'U DE G', 'Venados FC', 'Ninguno']
        },
        
        'Total Afición':{
            'skiprows' : 8, 
            'usecols':'EC:FJ',
            'columns': ['América', 'Atlas', 'Chivas(Guadalajara)', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados (Monterrey)', 'Santos', 'Toluca', 'León', 'Tijuana', 'Mazatlán FC', 'Puebla', 'Pachuca', 'Querétaro', 'Necaxa', 'FC Juárez', 'Atlético San Luis', 'Alebrijes de Oaxaca', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Club Atlético Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico M Fútbol Club', 'U DE G', 'Venados FC']
        },      

        'Nivel Afición':{
            'skiprows' : 8, 
            'usecols':'FK:FM',
            'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        },      

        'Nivel Afición - Nuevos':{
            'skiprows' : 8, 
            'usecols':'FN:FP',
            'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        },      

        'Fan Base':{
            'skiprows' : 8, 
            'usecols':'FQ:FS',
            'columns': ['FAN BASE 1', 'FAN BASE 2', 'FAN BASE 3'] 
        },      
        
        'Liga':{
            'skiprows' : 8, 
            'usecols':'FT:FV',
            'columns': ['LIGA MX', 'ASCENSO MX', 'LIGA MX + ASCENSO MX']
        },      
        
        'Practica Futbol':{
            'skiprows' : 8, 
            'usecols':'FW:FZ',
            'columns': ['NO PRACTICA', 'SÍ PRACTICA', 'SI, A VECES', 'SÍ, SIEMPRE / FRECUENTE']
        },      
        
        'Presencia de niños':{
            'skiprows' : 8, 
            'usecols':'GA:GB',
            'columns': ['SÍ', 'NO']
        },      

        'Fans en la ciudad':{
            'skiprows' : 8, 
            'usecols':'GC:GP',
            'columns': ['AGUASCALIENTES', 'CIUDAD JUÁREZ', 'CDMX', 'GUADALAJARA', 'LEÓN', 'MONTERREY', 'MAZATLÁN', 'PACHUCA', 'PUEBLA', 'QUERÉTARO', 'SAN LUIS POTOSÍ', 'TIJUANA', 'TOLUCA', 'TORREÓN']
        },      
        
        'Milenials Aficionados':{
            'skiprows' : 8, 
            'usecols':'GQ:HH',
            'columns': ['AMÉRICA', 'ATLAS', 'CHIVAS', 'CRUZ AZUL', 'PUMAS', 'TIGRES', 'RAYADOS', 'SANTOS', 'TOLUCA', 'LEÓN', 'TIJUANA', 'MAZATLÁN', 'PUEBLA', 'PACHUCA', 'QUERÉTARO', 'FC JUÁREZ', 'ATLÉTICO SAN LUIS', 'NECAXA']
        },      

        'Productos Bancarios':{
            'skiprows' : 8, 
            'usecols':'HI:HK',
            'columns': ['TARJETA DE DÉBITO', 'TARJETA DE CRÉDITO', 'BANCO EN LINEA']
        },      
        
        
        'BBVA Bancomer':{
            'skiprows' : 8, 
            'usecols':'HL:HM',
            'columns': ['CLIENTES BBVA BANCOMER', 'OTROS BANCOS']
        },      
        
        
        'Apuestas Deportivas':{
            'skiprows' : 8, 
            'usecols':'HN:HO',
            'columns': ['SÍ', 'NO']
        },     
        
        'Caliente':{
            'skiprows' : 8, 
            'usecols':'HP:HQ',
            'columns': ['CONOCE', 'USA']
        },      
        
    }
}


sheet_dict = xls_dict[2020]
df_year = pd.DataFrame()
for sheet  in tqdm(sheet_names):
    if sheet not in ['Contents', 'MUESTRA', 'Q1B', 'Q2BEDAD']:
        df_answ = pd.read_excel(xls, sheet_name=sheet, skiprows = sheet_dict['answers']['skiprows'], usecols = sheet_dict['answers']['usecols'])
        question = pd.read_excel(xls, sheet_name=sheet, skiprows = sheet_dict['question']['skiprows'], usecols = sheet_dict['question']['usecols']).columns[0]

        #Rename the column
        df_answ.columns = [question]
        #We just want to include the answer to the question not the statistical values
        for cutword  in sheet_dict['answers']['cutwords']:
            df_cut = df_answ[ df_answ[question].replace(np.nan, '').str.startswith(cutword) ]
            if len(df_cut)>0:
                cutindex = df_cut.index[0]
                break
        #We cut the df at the cutword index position
        df_answ = df_answ[:cutindex]
        #We only want the values asociated with the anwers not the statistical values
        df_answ = df_answ.dropna()
        valuesindex = df_answ.index

        df_question = pd.DataFrame()
        for demograpphic in tqdm(sheet_dict.keys()):
            if demograpphic in ['question', 'answers', 'questions_list']:
                continue
            else:
                df = pd.read_excel(xls, sheet_name=sheet, skiprows = sheet_dict[demograpphic]['skiprows'], usecols = sheet_dict[demograpphic]['usecols'])
                df = df.loc[valuesindex]
                df.columns = sheet_dict[demograpphic]['columns']
                df = df_answ.join(df)
                df[question] = df[question].apply(lambda x: question  + ' - ' + x)
                df['pregunta'] =  question
                df = df.set_index(question)
                df = df.transpose()
                df = df.reset_index()
                df = df.rename(columns ={'index':'demographic_values'})
                df['demographic'] = demograpphic
                
                if len(df_question) == 0:
                    df_question = df
                else:
                    df_question = df_question.append(df)
                
        if len(df_year) == 0:
            df_year = df_question
        else:
            df_year = df_year.merge(df_question, on=['demographic', 'demographic_values'])
            
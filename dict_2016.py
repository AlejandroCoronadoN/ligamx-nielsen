dict_2016 = {
        
        'answers': {
            'skiprows' : 7, 
            'usecols':'A:A',
            'cutword': ['Columns Tested', 'Mediana', 'Sub-total',  'Muestra']
        },
        
        'question': {
            'skiprows' : 0, 
            'usecols':'A:A'
        },
        
        'sexo':{
            'skiprows' : 7, 
            'usecols':'AK:AL',
            'columns': ['Hombre',	'Mujer']
        },
        
        #'generacion':{
        #    'skiprows' : 7, 
        #    'usecols':'GG:GK',
        #    'columns': ['Milenials 18-25 años', 	'Milenials 26-35 años', 'No milenials 35-45 años']
        #,
        
        'edad':{
            'skiprows' : 7, 
            'usecols':'AF:AJ',
            'columns': ['18-25',	'26-35',  '36-45', 	'46-55', 	'56+']
        },
        
        'NSE':{
            'skiprows' : 7, 
            'usecols':'AM:AQ',
            'columns': ['AB', 	'C+', 'C', 'C-', 'D+/D/E']
        }, 

        'Ciudades':{
            'skiprows' : 7, 
            'usecols':'C:AE',
            'columns':['Aguascalientes', 'Cancún', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'Colima', 'CDMX', 'Guadalajara', 'Hermosillo', 'León', 'Los Mochis', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'Tampico', 'Tapachula', 'Tepic', 'Tijuana', 'Toluca', 'Torreón', 'Tuxtla Gutiérrez', 'Veracruz', 'Zacatecas', 'Zacatepec']
        },

        'Equipo Favorito':{
            'skiprows' : 7, 
            'usecols':'AR:CB',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Jaguares', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Coras FC', 'Correcaminos', 'Dorados', 'FC Juárez', 'Lobos BUAP', 'Loros de Colima', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },
        
        'Segundo Equipo':{
            'skiprows' : 7, 
            'usecols':'CC:DM',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Jaguares', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Coras FC', 'Correcaminos', 'Dorados', 'FC Juárez', 'Lobos BUAP', 'Loros de Colima', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },
        
        'Equipo Segunda':{
            'skiprows' : 7,     
            'usecols':'DN:EX',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Jaguares', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Coras FC', 'Correcaminos', 'Dorados', 'FC Juárez', 'Lobos BUAP', 'Loros de Colima', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },
        
        'Total Afición':{
            'skiprows' : 7, 
            'usecols':'FH:GR',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Jaguares', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Coras FC', 'Correcaminos', 'Dorados', 'FC Juárez', 'Lobos BUAP', 'Loros de Colima', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },      

        'Nivel Afición':{
            'skiprows' : 7, 
            'usecols':'EY:FA',
            'columns': ['Heavy', 'Medium', 'Light']
        },      

        #'Nivel Afición - Nuevos':{
        #   'skiprows' : 7, 
        #    'usecols':'FN:FP',
        #    'columns': ['Heavy', 'Medium', 'Light']
        #},      

        'Fan Base':{
            'skiprow    s' : 8, 
            'usecols':'FB:FD',
            'columns':  ['Fan base 1', 'Fan base 2', 'Fan base 3']
        },      
        
        'Liga':{
            'skiprows' : 7, 
            'usecols':'FE:FG',
            'columns': ['Liga MX', 'Ascenso MX', 'Liga MX and Ascenso MX']
        },      
        
        #'Practica Futbol':{
        #    'skiprows' : 7, 
        #    'usecols':'GM:GN',
        #    'columns': ['Si practica', 'No practica']
        #},      
    
        #'Tipo de Levantamiento':{
        #    'skiprows' : 7, 
        #    'usecols':'GV:GW',
        #    'columns': ['CELDA GP', 'CELDA BOOSTER']
        #},      
        
        #'Fan DNA':{
        #    'skiprows' : 7, 
        #    'usecols':'GX:HD',
        #    'columns': ['CELDA GP', 'CELDA BOOSTER']
        #},      
            
        #'Presencia de niños':{
        #    'skiprows' : 7, 
        #    'usecols':'GA:GB',
        #    'columns': [True, False]
        #},      

        #'Fans en la ciudad':{
        #    'skiprows' : 7, 
        #    'usecols':'GP:HP',
        #    'columns': []
        #},      
        
        #'Milenials Aficionados':{
        #    'skiprows' : 7, 
        #    'usecols':'HR:IX',
        #    'columns': []
        #},      

        #'Productos Bancarios':{
        #    'skiprows' : 7, 
        #    'usecols':'GN:GP',
        #    'columns': ['Tarjeta de débito', 'Tarjeta de crédito','Banco en línea']
        #},      
        
        #'BBVA Bancomer':{
        #    'skiprows' : 7, 
        #    'usecols':'GQ:GR',
        #    'columns': ['Clientes BBVA Bancomer','Otros Bancos']
        #},      

        #'Segmentación':{
        #    'skiprows' : 7, 
        #    'usecols':'GK:GN    ',
        #    'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        #},     
        
        #'Apuestas Deportivas':{
        #    'skiprows' : 7, 
        #    'usecols':'HN:HO',
        #    'columns': [True, False]
        #},     
        
        #'Caliente':{
        #    'skiprows' : 7, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}

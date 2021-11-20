dict_2018 ={
        
        'answers': {
            'skiprows' : 9, 
            'usecols':'B:B',
            'cutword': ['Columns Tested', 'Mediana', 'Sub-total',  'Muestra']
        },
        
        'question': {
            'skiprows' : 2, 
            'usecols':'B:B'
        },
        
        'sexo':{
            'skiprows' : 9, 
            'usecols':'D:E',
            'columns': ['Hombre',	'Mujer']
        },
        
        #'generacion':{
        #    'skiprows' : 9, 
        #    'usecols':'GG:GK',
        #    'columns': ['Milenials 18-25 años', 	'Milenials 26-35 años', 'No milenials 35-45 años']
        #},
        
        'edad':{
            'skiprows' : 9, 
            'usecols':'F:K',
            'columns': ['18-25',	'26-35',  '36-45', 	'46-55', 	'56+']
        },
        
        'NSE':{
            'skiprows' : 9, 
            'usecols':'L:R',
            'columns': ['AB', 	'C+', 'C', 'C-', 'D+/D/E']
        }, 

        'Ciudades':{
            'skiprows' : 9, 
            'usecols':'Z:AY',
            'columns':['Aguascalientes', 'Cancún', 'CDMX', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'Guadalajara', 'Hermosillo', 'León', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tapachula', 'Tijuana', 'Toluca', 'Torreón', 'Veracruz', 'Zacatecas', 'Zacatepec']
        },

        'Equipo Favorito':{
            'skiprows' : 9, 
            'usecols':'AZ:CF',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec']
        },
        
        'Segundo Equipo':{
            'skiprows' : 9, 
            'usecols':'CG:DN',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },
        
        'Equipo Segunda':{
            'skiprows' : 9,     
            'usecols':'DO:EV',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },
        
        'Total Afición':{
            'skiprows' : 9, 
            'usecols':'EW:GC',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec']
        },      

        'Nivel Afición':{
            'skiprows' : 9, 
            'usecols':'GS:GU',
            'columns': ['Heavy', 'Medium', 'Light']
        },      

        #'Nivel Afición - Nuevos':{
        #   'skiprows' : 9, 
        #    'usecols':'FN:FP',
        #    'columns': ['Heavy', 'Medium', 'Light']
        #},      

        'Fan Base':{
            'skiprow    s' : 8, 
            'usecols':'GD:GF',
            'columns':  ['Fan base 1', 'Fan base 2', 'Fan base 3']
        },      
        
        #'Liga':{
        #    'skiprows' : 9, 
        #    'usecols':'FT:FV',
        #    'columns': ['Liga MX', 'Ascenso MX', 'Liga MX and Ascenso MX']
        #},      
        
        'Practica Futbol':{
            'skiprows' : 9, 
            'usecols':'GM:GN',
            'columns': ['Si practica', 'No practica']
        },      
    
        'Tipo de Levantamiento':{
            'skiprows' : 9, 
            'usecols':'GV:GW',
            'columns': ['CELDA GP', 'CELDA BOOSTER']
        },      
        
        'Fan DNA':{
            'skiprows' : 9, 
            'usecols':'GX:HD',
            'columns': ['Cynical', 'Disengaged', 'Armchair fans', 'Connection Fans', 'Busy', 'Game experts', 'Trend Positives']
        },      
            
        #'Presencia de niños':{
        #    'skiprows' : 9, 
        #    'usecols':'GA:GB',
        #    'columns': [True, False]
        #},      

        #'Fans en la ciudad':{
        #    'skiprows' : 9, 
        #    'usecols':'GP:HP',
        #    'columns': []
        #},      
        
        #'Milenials Aficionados':{
        #    'skiprows' : 9, 
        #    'usecols':'HR:IX',
        #    'columns': []
        #},      

        'Productos Bancarios':{
            'skiprows' : 9, 
            'usecols':'GN:GP',
            'columns': ['Tarjeta de débito', 'Tarjeta de crédito','Banco en línea']
        },      
        
        'BBVA Bancomer':{
            'skiprows' : 9, 
            'usecols':'GQ:GR',
            'columns': ['Clientes BBVA Bancomer','Otros Bancos']
        },      

        #'Segmentación':{
        #    'skiprows' : 9, 
        #    'usecols':'GK:GN   ',
        #    'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        #},     
        
        #'Apuestas Deportivas':{
        #    'skiprows' : 9, 
        #    'usecols':'HN:HO',
        #    'columns': [True, False]
        #},     
        
        #'Caliente':{
        #    'skiprows' : 9, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}
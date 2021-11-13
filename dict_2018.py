test_dict = {
    
2018:{
        'questions_list': [], 
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
            'columns':['AGUASCALIENTES', 'CANCÚN', 'CDMX', 'CELAYA', 'CIUDAD JUÃREZ', 'CIUDAD VICTORIA', 'CULIACAN', 'GUADALAJARA', 'HERMOSILLO', 'LEÓN', 'MÉRIDA', 'MONTERREY', 'MORELIA', 'OAXACA', 'PACHUCA', 'PUEBLA', 'QUERÉTARO', 'SAN LUIS', 'TAMPICO', 'TAPACHULA', 'TIJUANA', 'TOLUCA', 'TORREÓN', 'VERACRUZ', 'ZACATECAS', 'ZACATEPEC']
        },

        'Equipo Favorito':{
            'skiprows' : 9, 
            'usecols':'AZ:CF',
            'columns': ['América', 'Atlas', 'Chivas(Guadalajara)', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados (Monterrey)', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz (Tiburones)', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros (Tapachula)', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juarez', 'Atlético San Luis', 'Mineros de Zacatecas', 'POTROS UAEM', 'Tampico M Fútbol Club', 'U DE G', 'Venados F.C', 'ZACATEPEC']
        },
        
        'Segundo Equipo':{
            'skiprows' : 9, 
            'usecols':'CG:DN',
            'columns': ['América', 'Atlas', 'Chivas(Guadalajara)', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados (Monterrey)', 'Santos', 'Toluca', 'Le ón', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz (Tiburones)', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros (Tapachula)', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC JUÃREZ', 'Atlético San Luis', 'Mineros de Zacatecas', 'POTROS UAEM', 'Tampico M Fútbol Club', 'U DE G', 'Venados F.C', 'ZACATEPEC', 'Ninguno']
        },
        
        'Equipo Segunda':{
            'skiprows' : 9,     
            'usecols':'DO:EV',
            'columns': ['América', 'Atlas', 'Chivas(Guadalajara)', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados (Monterrey)', 'Santos', 'Toluca', 'Le ón', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz (Tiburones)', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros (Tapachula)', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC JUÃREZ', 'Atlético San Luis', 'Mineros de Zacatecas', 'POTROS UAEM', 'Tampico M Fútbol Club', 'U DE G', 'Venados F.C', 'ZACATEPEC', 'Ninguno']
        },
        
        'Total Afición':{
            'skiprows' : 9, 
            'usecols':'EW:GC',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul ', 'Pumas ', 'Tigres', 'Rayados ', 'Santos ', 'Toluca', 'Le ón', 'Tijuana', 'Monarcas ', 'Puebla', 'Pachuca ', 'Querétaro ', 'Lobos BUAP', 'Veracruz ', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante ', 'Cafetaleros ', 'Cimarrones de Sonora FC  ', 'Club Celaya ', 'Correcaminos ', 'Dorados', 'FC JUÃREZ', 'Atlético San Luis (AA)', 'Mineros de Zacatecas(AB)', 'POTROS UAEM (AC)', 'Tampico M Fútbol Club(AD)', 'U DE G(AE)', 'Venados F.C(AF)', 'ZACATEPEC(AG)']
        },      

        'Nivel Afición':{
            'skiprows' : 9, 
            'usecols':'GS:GU',
            'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        },      

        #'Nivel Afición - Nuevos':{
        #   'skiprows' : 9, 
        #    'usecols':'FN:FP',
        #    'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        #},      

        'Fan Base':{
            'skiprow    s' : 8, 
            'usecols':'GD:GF',
            'columns': ['FAN BASE 1', 'FAN BASE 2', 'FAN BASE 3'] 
        },      
        
        #'Liga':{
        #    'skiprows' : 9, 
        #    'usecols':'FT:FV',
        #    'columns': ['LIGA MX', 'ASCENSO MX', 'LIGA MX + ASCENSO MX']
        #},      
        
        'Practica Futbol':{
            'skiprows' : 9, 
            'usecols':'GM:GN',
            'columns': ['SÍ PRACTICA', 'NO PRACTICA']
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
        #    'columns': ['SÍ', 'NO']
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
            'columns': ['TARJETA DE DÉBITO', 'TARJETA DE CRÉDITO', 'BANCO EN LINEA']
        },      
        
        'BBVA Bancomer':{
            'skiprows' : 9, 
            'usecols':'GQ:GR',
            'columns': ['CLIENTES BBVA BANCOMER', 'OTROS BANCOS']
        },      

        #'Segmentación':{
        #    'skiprows' : 9, 
        #    'usecols':'GK:GN    ',
        #    'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        #},     
        
        #'Apuestas Deportivas':{
        #    'skiprows' : 9, 
        #    'usecols':'HN:HO',
        #    'columns': ['SÍ', 'NO']
        #},     
        
        #'Caliente':{
        #    'skiprows' : 9, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}


}
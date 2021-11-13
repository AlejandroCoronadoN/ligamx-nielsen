test_dict = {
    
2016:{
        'questions_list': [], 
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
        #},
        
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
            'columns':['Aguascalientes', 'Cancún', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'Colima', 'DF', 'Guadalajara', 'Hermosillo', 'León', 'Los Mochis', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'Tampico', 'Tapachula', 'Tepic', 'Tijuana', 'Toluca', 'Torreón', 'Tuxtla Gutiérrez', 'Veracruz', 'Zacatecas', 'Zacatepec']
        },

        'Equipo Favorito':{
            'skiprows' : 7, 
            'usecols':'AR:CB',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Jaguares', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Coras FC', 'Correcaminos', 'Dorados', 'FC Juárez', 'Lobos BUAP', 'Loros de Colima', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'TM Fútbol Club', 'U de G', 'Venados F.C.', 'Zacatepec Siglo 21', 'Ninguno']
        },
        
        'Segundo Equipo':{
            'skiprows' : 7, 
            'usecols':'CC:DM',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Jaguares', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Coras FC', 'Correcaminos', 'Dorados', 'FC Juárez', 'Lobos BUAP', 'Loros de Colima', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'TM Fútbol Club', 'U de G', 'Venados F.C.', 'Zacatepec Siglo 21', 'Ninguno']
        },
        
        'Equipo Segunda':{
            'skiprows' : 7,     
            'usecols':'DN:EX',
            'columns': ['América	Atlas	Chivas	Cruz Azul	Pumas	Tigres	Rayados	Santos	Toluca	León	Tijuana	Monarcas	Puebla	Pachuca	Querétaro	Jaguares	Veracruz	Necaxa	Alebrijes de Oaxaca	Atlante	Cafetaleros	Cimarrones de Sonora FC	Club Celaya	Coras FC	Correcaminos	Dorados	FC Juárez	Lobos BUAP	Loros de Colima	Mineros de Zacatecas	Murciélagos FC	Potros UAEM	TM Fútbol Club	U de G	Venados F.C.	Zacatepec Siglo 21	Ninguno']
        },
        
        'Total Afición':{
            'skiprows' : 7, 
            'usecols':'FH:GR',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Jaguares', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Coras FC', 'Correcaminos', 'Dorados', 'FC Juárez', 'Lobos BUAP', 'Loros de Colima', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'TM Fútbol Club', 'U de G', 'Venados F.C.', 'Zacatepec Siglo 21', 'Ninguno']
        },      

        'Nivel Afición':{
            'skiprows' : 7, 
            'usecols':'EY:FA',
            'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        },      

        #'Nivel Afición - Nuevos':{
        #   'skiprows' : 7, 
        #    'usecols':'FN:FP',
        #    'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        #},      

        'Fan Base':{
            'skiprow    s' : 8, 
            'usecols':'FB:FD',
            'columns': ['FAN BASE 1', 'FAN BASE 2', 'FAN BASE 3'] 
        },      
        
        'Liga':{
            'skiprows' : 7, 
            'usecols':'FE:FG',
            'columns': ['LIGA MX', 'ASCENSO MX', 'LIGA MX + ASCENSO MX']
        },      
        
        #'Practica Futbol':{
        #    'skiprows' : 7, 
        #    'usecols':'GM:GN',
        #    'columns': ['SÍ PRACTICA', 'NO PRACTICA']
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
        #    'columns': ['SÍ', 'NO']
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
        #    'columns': ['TARJETA DE DÉBITO', 'TARJETA DE CRÉDITO', 'BANCO EN LINEA']
        #},      
        
        #'BBVA Bancomer':{
        #    'skiprows' : 7, 
        #    'usecols':'GQ:GR',
        #    'columns': ['CLIENTES BBVA BANCOMER', 'OTROS BANCOS']
        #},      

        #'Segmentación':{
        #    'skiprows' : 7, 
        #    'usecols':'GK:GN    ',
        #    'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        #},     
        
        #'Apuestas Deportivas':{
        #    'skiprows' : 7, 
        #    'usecols':'HN:HO',
        #    'columns': ['SÍ', 'NO']
        #},     
        
        #'Caliente':{
        #    'skiprows' : 7, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}


}
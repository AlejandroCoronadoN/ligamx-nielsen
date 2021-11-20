dict_2015 = {
        
        'answers': {
           'skiprows' : 7, 
            'usecols':'A:A',
            'cutword': ['Columns Tested', 'Mediana', 'Sub-total',  'Muestra', 'Promedio:', 'Promedio']
        },
        
        'question': {
            'skiprows' : 0, 
            'usecols':'A:A'
        },
        
        'sexo':{
           'skiprows' : 7, 
            'usecols':'M:N',
            'columns': ['Hombre',	'Mujer']
        },
        
        #'generacion':{
        #   'skiprows' : 7, 
        #    'usecols':'GG:GK',
        #    'columns': ['Milenials 18-25 años', 	'Milenials 26-35 años', 'No milenials 35-45 años']
        #},
        
        'edad':{
           'skiprows' : 7, 
            'usecols':'H:L',
            'columns': ['18-25',	'26-35',  '36-45', 	'46-55', 	'56+']
        },
        
        'NSE':{
           'skiprows' : 7, 
            'usecols':'C:G',
            'columns': ['AB', 	'C+', 'C', 'C-', 'D+/D/E']
        }, 

        'Ciudades':{
           'skiprows' : 7, 
            'usecols':'O:AP',
            'columns':['Aguascalientes', 'Cancún', 'Celaya', 'Ciudad Juarez', 'Ciudad Victoria', 'Culiacán', 'Guadalajara', 'Hermosillo', 'León', 'Los Mochis', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Puebla', 'Pachuca', 'Querétaro', 'San Luis Potosí', 'Tapachula', 'Tepic', 'Tijuana', 'Toluca', 'Torreón', 'Tuxtla Gutierrez', 'Valle de México', 'Veracruz', 'Zacatecas', 'Zacatepec / Cuernavaca']
        },

        'Equipo Favorito':{
           'skiprows' : 7, 
            'usecols':'AQ:BX',
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Chivas', 'Jaguares', 'León', 'Rayados', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'Tigres', 'Pumas', 'Veracruz', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Celaya', 'Cimarrones', 'Coras FC', 'Correcaminos', 'FC Juárez', 'Lobos BUAP', 'Mineros de Zacatecas', 'Murcielagos', 'Necaxa', 'San Luis Potosí', 'UDG', 'Venados FC', 'Zacatepec']
            },
        
        'Segundo Equipo':{
           'skiprows' : 7, 
            'usecols':'BY:DF',
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Chivas', 'Jaguares', 'León', 'Rayados', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'Tigres', 'Pumas', 'Veracruz', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Celaya', 'Cimarrones', 'Coras FC', 'Correcaminos', 'FC Juárez', 'Lobos BUAP', 'Mineros de Zacatecas', 'Murcielagos', 'Necaxa', 'San Luis Potosí', 'UDG', 'Venados FC', 'Zacatepec']
            },
        
        'Equipo Segunda':{
           'skiprows' : 7,     
            'usecols':'DG:EN',
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Chivas', 'Jaguares', 'León', 'Rayados', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'Tigres', 'Pumas', 'Veracruz', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Celaya', 'Cimarrones', 'Coras FC', 'Correcaminos', 'FC Juárez', 'Lobos BUAP', 'Mineros de Zacatecas', 'Murcielagos', 'Necaxa', 'San Luis Potosí', 'UDG', 'Venados FC', 'Zacatepec']
            },
        
        'Total Afición':{
           'skiprows' : 7, 
            'usecols':'EO:FV',
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Chivas', 'Jaguares', 'León', 'Rayados', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'Tigres', 'Pumas', 'Veracruz', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Celaya', 'Cimarrones', 'Coras FC', 'Correcaminos', 'FC Juárez', 'Lobos BUAP', 'Mineros de Zacatecas', 'Murcielagos', 'Necaxa', 'San Luis Potosí', 'UDG', 'Venados FC', 'Zacatepec']
            },      

        'Nivel Afición':{
           'skiprows' : 7, 
            'usecols':'GA:GD',
            'columns': ['Hardcore','Heavy', 'Medium', 'Light']
        },      

        #'Nivel Afición - Nuevos':{
        #  'skiprows' : 7, 
        #    'usecols':'FN:FP',
        #    'columns': ['Heavy', 'Medium', 'Light']
        #},      

        'Fan Base':{
            'skiprows' : 7, 
            'usecols':'GE:GG',
            'columns':  ['Fan base 1', 'Fan base 2', 'Fan base 3']
        },      
        
        'Liga':{
           'skiprows' : 7, 
            'usecols':'GH:GI',
            'columns': ['Liga MX', 'Ascenso MX']
        },      
        
        #'Practica Futbol':{
        #   'skiprows' : 7, 
        #    'usecols':'GM:GN',
        #    'columns': ['Si practica', 'No practica']
        #},      
    
        #'Tipo de Levantamiento':{
        #   'skiprows' : 7, 
        #    'usecols':'GV:GW',
        #    'columns': ['CELDA GP', 'CELDA BOOSTER']
        #},      
        
        #'Fan DNA':{
        #   'skiprows' : 7, 
        #    'usecols':'GX:HD',
        #    'columns': ['CELDA GP', 'CELDA BOOSTER']
        #},      
            
        #'Presencia de niños':{
        #   'skiprows' : 7, 
        #    'usecols':'GA:GB',
        #    'columns': [True, False]
        #},      

        #'Fans en la ciudad':{
        #   'skiprows' : 7, 
        #    'usecols':'GP:HP',
        #    'columns': []
        #},      
        
        #'Milenials Aficionados':{
        #   'skiprows' : 7, 
        #    'usecols':'HR:IX',
        #    'columns': []
        #},      

        #'Productos Bancarios':{
        #   'skiprows' : 7, 
        #    'usecols':'GN:GP',
        #    'columns': ['Tarjeta de débito', 'Tarjeta de crédito','Banco en línea']
        #},      
        
        #'BBVA Bancomer':{
        #   'skiprows' : 7, 
        #    'usecols':'GQ:GR',
        #    'columns': ['Clientes BBVA Bancomer','Otros Bancos']
        #},      

        #'Segmentación':{
        #   'skiprows' : 7, 
        #    'usecols':'GK:GN    ',
        #    'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        #},     
        
        #'Apuestas Deportivas':{
        #   'skiprows' : 7, 
        #    'usecols':'HN:HO',
        #    'columns': [True, False]
        #},     
        
        #'Caliente':{
        #   'skiprows' : 7, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}



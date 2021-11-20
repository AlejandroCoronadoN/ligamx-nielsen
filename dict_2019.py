dict_2019 = {
        
        'answers': {
            'skiprows' : 8, 
            'usecols':'A:A',
            'cutword': ['Columns Tested', 'Mediana', 'Sub-total',  'Muestra']
        },
        
        'question': {
            'skiprows' : 0, 
            'usecols':'A:A'
        },
        
        'sexo':{
            'skiprows' : 8, 
            'usecols':'C:D',
            'columns': ['Hombre',	'Mujer']
        },
        
        #'generacion':{
        #    'skiprows' : 8, 
        #    'usecols':'F:G',
        #    'columns': ['Milenials', 	'No milenials']
        #},
        
        'edad':{
            'skiprows' : 8, 
            'usecols':'I:M',
            'columns': ['18-25',	'26-35',  '36-45', 	'46-55', 	'56+']
        },
        
        'NSE':{
            'skiprows' : 8, 
            'usecols':'O:S',
            'columns': ['AB', 	'C+', 'C', 'C-', 'D+/D/E']
        }, 

        'Ciudad':{
            'skiprows' : 8, 
            'usecols':'U:AU',
            'columns': ['Aguascalientes', 'Cancún', 'CDMX', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'Guadalajara', 'Hermosillo', 'León', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tuxtla Gutiérrez', 'Tijuana', 'Toluca', 'Torreón', 'Veracruz', 'Zacatecas', 'Zacatepec', 'Colima']
        },

        'Equipo Favorito':{
            'skiprows' : 8, 
            'usecols':'AW:CC',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Loros de Colima', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec']
        },
        
        'Segundo Equipo':{
            'skiprows' : 8, 
            'usecols':'CE:DL',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Loros de Colima', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },
        
        'Equipo Segunda':{
            'skiprows' : 8, 
            'usecols':'DN:EB',
            'columns': ['Loros de Colima', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },
        
        'Total Afición':{
            'skiprows' : 8, 
            'usecols':'ED:FJ',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Loros de Colima', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec']
        },      

        'Nivel Afición':{
            'skiprows' : 8, 
            'usecols':'FL:FN',
            'columns': ['Heavy', 'Medium', 'Light']
        },      

        #'Nivel Afición - Nuevos':{
        #   'skiprows' : 8, 
        #    'usecols':'FN:FP',
        #    'columns': ['Heavy', 'Medium', 'Light']
        #},      

        'Fan Base':{
            'skiprow    s' : 8, 
            'usecols':'FP:FR',
            'columns':  ['Fan base 1', 'Fan base 2', 'Fan base 3']
        },      
        
        'Liga':{
            'skiprows' : 8, 
            'usecols':'FT:FV',
            'columns': ['Liga MX', 'Ascenso MX', 'Liga MX and Ascenso MX']
        },      
        
        'Practica Futbol':{
            'skiprows' : 8, 
            'usecols':'FX:FY',
            'columns': ['No practica', 'Si practica']
        },      
        
        'Presencia de niños':{
            'skiprows' : 8, 
            'usecols':'GA:GB',
            'columns': [True, False]
        },      

        'Fans en la ciudad':{
            'skiprows' : 8, 
            'usecols':'GP:HP',
            'columns': ['Aguascalientes', 'Cancún', 'CDMX', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'Guadalajara', 'Hermosillo', 'León', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tuxtla Gutiérrez', 'Tijuana', 'Toluca', 'Torreón', 'Veracruz', 'Zacatecas', 'Zacatepec', 'Colima']
        },      
        
        'Milenials Aficionados':{
            'skiprows' : 8, 
            'usecols':'HR:IX',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Loros de Colima', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec']
        },      

        'Productos Bancarios':{
            'skiprows' : 8, 
            'usecols':'GD:GF',
            'columns': ['Tarjeta de débito', 'Tarjeta de crédito','Banco en línea']
        },      
        
        'BBVA Bancomer':{
            'skiprows' : 8, 
            'usecols':'GH:GI',
            'columns': ['Clientes BBVA Bancomer','Otros Bancos']
        },      

        'Segmentación':{
            'skiprows' : 8, 
            'usecols':'GK:GN',
            'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        },     
        
        #'Apuestas Deportivas':{
        #    'skiprows' : 8, 
        #    'usecols':'HN:HO',
        #    'columns': [True, False]
        #},     
        
        #'Caliente':{
        #    'skiprows' : 8, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}
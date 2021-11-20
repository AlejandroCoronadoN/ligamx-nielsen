dict_2017 = {
        
        'answers': {
            'skiprows' : 8, 
            'usecols':'A:A',
            'cutword': ['Columns Tested', 'Mediana', 'Sub-total',  'Muestra', 'Promedio:', 'Promedio']
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
        
        'generacion':{
           'skiprows' : 8, 
            'usecols':'F:G',
            'columns': ['Milenials', 	'No Milenials']
        },
        
        'edad':{
            'skiprows' : 8, 
            'usecols':'H:L',
            'columns': ['18-25',	'26-35',  '36-45', 	'46-55', 	'56+']
        },
        
        'NSE':{
            'skiprows' : 8, 
            'usecols':'N:R',
            'columns': ['AB', 	'C+', 'C', 'C-', 'D+/D/E']
        }, 

        'Ciudades':{
            'skiprows' : 8, 
            'usecols':'T:AT',
            'columns':['Aguascalientes', 'Cancún', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'CDMX', 'Guadalajara', 'Hermosillo', 'León', 'Los Mochis', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tapachula', 'Tijuana', 'Toluca', 'Torreón', 'Veracruz', 'Zacatecas', 'Zacatepec']
        },

        'Equipo Favorito':{
            'skiprows' : 8, 
            'usecols':'AV:CD',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
     },
        
        'Segundo Equipo':{
            'skiprows' : 8, 
            'usecols':'CF:DN',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
            },
        
        'Equipo Segunda':{
            'skiprows' : 8,     
            'usecols':'DP:EX',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
            },
        
        'Total Afición':{
            'skiprows' : 8, 
            'usecols':'EZ:GH',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno'] 
            },      

        'Nivel Afición':{
            'skiprows' : 8, 
            'usecols':'GJ:GL',
            'columns': ['Heavy', 'Medium', 'Light']
        },      

        #'Nivel Afición - Nuevos':{
        #   'skiprows' : 8, 
        #    'usecols':'FN:FP',
        #    'columns': ['Heavy', 'Medium', 'Light']
        #},      

        'Fan Base':{
            'skiprow    s' : 8, 
            'usecols':'GN:GP',
            'columns':  ['Fan base 1', 'Fan base 2', 'Fan base 3']
        },      
        
        'Liga':{
            'skiprows' : 8, 
            'usecols':'GR:  GT',
            'columns': ['Liga MX', 'Ascenso MX', 'Liga MX and Ascenso MX']
        },      

        'Relación con el futbol':{
            'skiprows' : 8, 
            'usecols':'GV:  GW',
            'columns': ['Ocasional', 'Aficionado' ]
        },      
        
        'Consume Refresco':{
            'skiprows' : 8, 
            'usecols':'HB:  HC',
            'columns': ['Si', 'No' ]
        },      

        'Marca refresco':{
            'skiprows' : 8, 
            'usecols':'HE:  HF',
            'columns': ['Coca Cola', 'Otro' ]
        }, 
        
        'Consume refresco en el estadio':{
            'skiprows' : 8, 
            'usecols':'HH:  HI',
            'columns': ['Si', 'No' ]
        }, 
        
        'Practica Futbol':{
            'skiprows' : 8, 
            'usecols':'GY:GZ',
            'columns': ['No practica', 'Si practica']
        },      
    
        #'Tipo de Levantamiento':{
        #    'skiprows' : 8, 
        #    'usecols':'GV:GW',
        #    'columns': ['CELDA GP', 'CELDA BOOSTER']
        #},      
        
        #'Fan DNA':{
        #    'skiprows' : 8, 
        #    'usecols':'GX:HD',
        #    'columns': ['CELDA GP', 'CELDA BOOSTER']
        #},      
            
        #'Presencia de niños':{
        #    'skiprows' : 8, 
        #    'usecols':'GA:GB',
        #    'columns': [True, False]
        #},      

        'Fans en la ciudad':{
            'skiprows' : 8, 
            'usecols':'IS:KA',
            'columns': ['Aguascalientes', 'Cancún', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'CDMX', 'Guadalajara', 'Hermosillo', 'León', 'Los Mochis', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tapachula', 'Tijuana', 'Toluca', 'Torreón', 'Veracruz', 'Zacatecas', 'Zacatepec']
        },      
        
        'Milenials Aficionados':{
            'skiprows' : 8, 
            'usecols':'HR:IX',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Zacatepec', 'Ninguno']
        },      

        #'Productos Bancarios':{
        #    'skiprows' : 8, 
        #    'usecols':'GN:GP',
        #    'columns': ['Tarjeta de débito', 'Tarjeta de crédito','Banco en línea']
        #},      
        
        #'BBVA Bancomer':{
        #    'skiprows' : 8, 
        #    'usecols':'GQ:GR',
        #    'columns': ['Clientes BBVA Bancomer','Otros Bancos']
        #},      

        'Segmentación':{
            'skiprows' : 8, 
            'usecols':'KC:KF',
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
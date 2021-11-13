test_dict = {
    
2017:{
        'questions_list': [], 
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
            'columns': ['MILENIALS', 	'NO MILENIALS']
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
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero', 'U de G', 'Venados F.C', 'Zacatepec', 'Ninguno']
     },
        
        'Segundo Equipo':{
            'skiprows' : 8, 
            'usecols':'CF:DN',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero', 'U de G', 'Venados F.C', 'Zacatepec', 'Ninguno']
            },
        
        'Equipo Segunda':{
            'skiprows' : 8,     
            'usecols':'DP:EX',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero', 'U de G', 'Venados F.C', 'Zacatepec', 'Ninguno']
            },
        
        'Total Afición':{
            'skiprows' : 8, 
            'usecols':'EZ:GH',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero', 'U de G', 'Venados F.C', 'Zacatepec', 'Ninguno'] 
            },      

        'Nivel Afición':{
            'skiprows' : 8, 
            'usecols':'GJ:GL',
            'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        },      

        #'Nivel Afición - Nuevos':{
        #   'skiprows' : 8, 
        #    'usecols':'FN:FP',
        #    'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        #},      

        'Fan Base':{
            'skiprow    s' : 8, 
            'usecols':'GN:GP',
            'columns': ['FAN BASE 1', 'FAN BASE 2', 'FAN BASE 3'] 
        },      
        
        'Liga':{
            'skiprows' : 8, 
            'usecols':'GR:  GT',
            'columns': ['LIGA MX', 'ASCENSO MX', 'LIGA MX + ASCENSO MX']
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
            'columns': ['NO PRACTICA', 'Sí PRACTICA']
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
        #    'columns': ['SÍ', 'NO']
        #},      

        'Fans en la ciudad':{
            'skiprows' : 8, 
            'usecols':'IS:KA',
            'columns': ['Aguascalientes', 'Cancún', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'CDMX', 'Guadalajara', 'Hermosillo', 'León', 'Los Mochis', 'Mérida', 'Monterrey', 'Morelia', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tapachula', 'Tijuana', 'Toluca', 'Torreón', 'Veracruz', 'Zacatecas', 'Zacatepec']
        },      
        
        'Milenials Aficionados':{
            'skiprows' : 8, 
            'usecols':'HR:IX',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Monarcas', 'Puebla', 'Pachuca', 'Querétaro', 'Lobos BUAP', 'Veracruz', 'Necaxa', 'Alebrijes de Oaxaca', 'Atlante', 'Cafetaleros', 'Cimarrones de Sonora FC', 'Club Celaya', 'Correcaminos', 'Dorados', 'FC Juárez', 'Atlético San Luis', 'Mineros de Zacatecas', 'Murciélagos FC', 'Potros UAEM', 'Tampico Madero', 'U de G', 'Venados F.C', 'Zacatepec', 'Ninguno']
        },      

        #'Productos Bancarios':{
        #    'skiprows' : 8, 
        #    'usecols':'GN:GP',
        #    'columns': ['TARJETA DE DÉBITO', 'TARJETA DE CRÉDITO', 'BANCO EN LINEA']
        #},      
        
        #'BBVA Bancomer':{
        #    'skiprows' : 8, 
        #    'usecols':'GQ:GR',
        #    'columns': ['CLIENTES BBVA BANCOMER', 'OTROS BANCOS']
        #},      

        'Segmentación':{
            'skiprows' : 8, 
            'usecols':'KC:KF',
            'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        },     
        
        #'Apuestas Deportivas':{
        #    'skiprows' : 8, 
        #    'usecols':'HN:HO',
        #    'columns': ['SÍ', 'NO']
        #},     
        
        #'Caliente':{
        #    'skiprows' : 8, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}


}
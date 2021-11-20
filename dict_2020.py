dict_2020 = {
        
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
            'columns': ['Aguascalientes', 'Cancún', 'CDMX', 'Celaya', 'Ciudad Juárez', 'Ciudad Victoria', 'Culiacán', 'Guadalajara', 'Hermosillo', 'León', 'Mazatlán', 'Mérida', 'Morelia', 'Monterrey', 'Oaxaca', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tampico', 'Tepatitlán', 'Tijuana', 'Tlaxcala', 'Toluca', 'Torreón', 'Villa Hermosa', 'Zacatecas', 'Resto']
        },

        'Equipo Favorito':{
            'skiprows' : 8, 
            'usecols':'AT:CB',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Mazatlán FC', 'Puebla', 'Pachuca', 'Querétaro', 'Necaxa', 'FC Juárez', 'Atlético San Luis', 'Alebrijes', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Ninguno']
        },
        
        'Segundo Equipo':{
            'skiprows' : 8, 
            'usecols':'CC:DK',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Mazatlán FC', 'Puebla', 'Pachuca', 'Querétaro', 'Necaxa', 'FC Juárez', 'Atlético San Luis', 'Alebrijes', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Ninguno']
        },
        
        'Equipo Segunda':{
            'skiprows' : 8, 
            'usecols':'DL:EB',
            'columns': ['Alebrijes', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico Madero FC', 'U de G', 'Venados FC', 'Ninguno']
        },
        
        'Total Afición':{
            'skiprows' : 8, 
            'usecols':'EC:FJ',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Mazatlán FC', 'Puebla', 'Pachuca', 'Querétaro', 'Necaxa', 'FC Juárez', 'Atlético San Luis', 'Alebrijes', 'Atlante', 'Cancún FC', 'Cimarrones de Sonora FC', 'Morelia', 'Club Celaya', 'Correcaminos', 'Dorados', 'Mineros de Zacatecas', 'Pumas Tabasco', 'Tapatío', 'Tepatitlán FC', 'Tlaxcala FC', 'Tampico Madero FC', 'U de G', 'Venados FC']
        },      

        'Nivel Afición':{
            'skiprows' : 8, 
            'usecols':'FK:FM',
            'columns': ['Heavy', 'Medium', 'Light']
        },      

        'Nivel Afición - Nuevos':{
            'skiprows' : 8, 
            'usecols':'FN:FP',
            'columns': ['Heavy', 'Medium', 'Light']
        },      

        'Fan Base':{
            'skiprows' : 8, 
            'usecols':'FQ:FS',
            'columns':  ['Fan base 1', 'Fan base 2', 'Fan base 3']
        },      
        
        'Liga':{
            'skiprows' : 8, 
            'usecols':'FT:FV',
            'columns': ['Liga MX', 'Ascenso MX', 'Liga MX and Ascenso MX']
        },      
        
        'Practica Futbol':{
            'skiprows' : 8, 
            'usecols':'FW:FZ',
            'columns': ['No practica', 'Si practica', 'A veces practiva', 'Practica frecuente']
        },      
        
        'Presencia de niños':{
            'skiprows' : 8, 
            'usecols':'GA:GB',
            'columns': [True, False]
        },      

        'Fans en la ciudad':{
            'skiprows' : 8, 
            'usecols':'GC:GP',
            'columns': ['Aguascalientes', 'Ciudad Juárez', 'CDMX', 'Guadalajara', 'León', 'Monterrey', 'Mazatlán', 'Pachuca', 'Puebla', 'Querétaro', 'San Luis Potosí', 'Tijuana', 'Toluca', 'Torreón']
        },      
        
        'Milenials Aficionados':{
            'skiprows' : 8, 
            'usecols':'GQ:HH',
            'columns': ['América', 'Atlas', 'Chivas', 'Cruz Azul', 'Pumas', 'Tigres', 'Rayados', 'Santos', 'Toluca', 'León', 'Tijuana', 'Mazatlán', 'Puebla', 'Pachuca', 'Querétaro', 'FC Juárez', 'Atlético San Luis', 'Necaxa']
        },      

        'Productos Bancarios':{
            'skiprows' : 8, 
            'usecols':'HI:HK',
            'columns': ['Tarjeta de débito', 'Tarjeta de crédito','Banco en línea']
        },      
        
        
        'BBVA Bancomer':{
            'skiprows' : 8, 
            'usecols':'HL:HM',
            'columns': ['Clientes BBVA Bancomer','Otros Bancos']
        },      
        
        'Apuestas Deportivas':{
            'skiprows' : 8, 
            'usecols':'HN:HO',
            'columns': [True, False]
        },     
        
        'Caliente':{
            'skiprows' : 8, 
            'usecols':'HP:HQ',
            'columns': ['CONOCE', 'USA']
        },      
        
    }
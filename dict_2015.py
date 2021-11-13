test_dict = {
    
2015:{
        'questions_list': [], 
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
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Guadalajara (Chivas)', 'Jaguares (Chiapas)', 'León', 'Monterrey (Rayados)', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'UANL (Tigres)', 'UNAM (Pumas)', 'Veracruz (Tiburones)', 'Alebrijes (Oaxaca)', 'Atlante', 'Cafetaleros (Tapachula)', 'Celaya', 'Cimarrones (Sonora)', 'Coras FC (Tepic)', 'Correcaminos', 'FC Juarez', 'Lobos BUAP', 'Mineros (Zacatecas)', 'Murcielagos (Mochis)', 'Necaxa', 'San Luis', 'UDG (Leones Negros)', 'Venados (Mérida)', 'Zacatepec']
            },
        
        'Segundo Equipo':{
           'skiprows' : 7, 
            'usecols':'BY:DF',
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Guadalajara (Chivas)', 'Jaguares (Chiapas)', 'León', 'Monterrey (Rayados)', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'UANL (Tigres)', 'UNAM (Pumas)', 'Veracruz (Tiburones)', 'Alebrijes (Oaxaca)', 'Atlante', 'Cafetaleros (Tapachula)', 'Celaya', 'Cimarrones (Sonora)', 'Coras FC (Tepic)', 'Correcaminos', 'FC Juarez', 'Lobos BUAP', 'Mineros (Zacatecas)', 'Murcielagos (Mochis)', 'Necaxa', 'San Luis', 'UDG (Leones Negros)', 'Venados (Mérida)', 'Zacatepec']
            },
        
        'Equipo Segunda':{
           'skiprows' : 7,     
            'usecols':'DG:EN',
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Guadalajara (Chivas)', 'Jaguares (Chiapas)', 'León', 'Monterrey (Rayados)', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'UANL (Tigres)', 'UNAM (Pumas)', 'Veracruz (Tiburones)', 'Alebrijes (Oaxaca)', 'Atlante', 'Cafetaleros (Tapachula)', 'Celaya', 'Cimarrones (Sonora)', 'Coras FC (Tepic)', 'Correcaminos', 'FC Juarez', 'Lobos BUAP', 'Mineros (Zacatecas)', 'Murcielagos (Mochis)', 'Necaxa', 'San Luis', 'UDG (Leones Negros)', 'Venados (Mérida)', 'Zacatepec']
            },
        
        'Total Afición':{
           'skiprows' : 7, 
            'usecols':'EO:FV',
            'columns': ['América', 'Atlas', 'Cruz Azul', 'Dorados', 'Guadalajara (Chivas)', 'Jaguares (Chiapas)', 'León', 'Monterrey (Rayados)', 'Morelia', 'Pachuca', 'Puebla', 'Querétaro', 'Santos', 'Tijuana', 'Toluca', 'UANL (Tigres)', 'UNAM (Pumas)', 'Veracruz (Tiburones)', 'Alebrijes (Oaxaca)', 'Atlante', 'Cafetaleros (Tapachula)', 'Celaya', 'Cimarrones (Sonora)', 'Coras FC (Tepic)', 'Correcaminos', 'FC Juarez', 'Lobos BUAP', 'Mineros (Zacatecas)', 'Murcielagos (Mochis)', 'Necaxa', 'San Luis', 'UDG (Leones Negros)', 'Venados (Mérida)', 'Zacatepec']
            },      

        'Nivel Afición':{
           'skiprows' : 7, 
            'usecols':'GA:GD',
            'columns': ['HARDCORE','HEAVY', 'MEDIUM', 'LIGHT']
        },      

        #'Nivel Afición - Nuevos':{
        #  'skiprows' : 7, 
        #    'usecols':'FN:FP',
        #    'columns': ['HEAVY', 'MEDIUM', 'LIGHT']
        #},      

        'Fan Base':{
            'skiprows' : 7, 
            'usecols':'GE:GG',
            'columns': ['FAN BASE 1', 'FAN BASE 2', 'FAN BASE 3'] 
        },      
        
        'Liga':{
           'skiprows' : 7, 
            'usecols':'GH:GI',
            'columns': ['LIGA MX', 'ASCENSO MX']
        },      
        
        #'Practica Futbol':{
        #   'skiprows' : 7, 
        #    'usecols':'GM:GN',
        #    'columns': ['SÍ PRACTICA', 'NO PRACTICA']
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
        #    'columns': ['SÍ', 'NO']
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
        #    'columns': ['TARJETA DE DÉBITO', 'TARJETA DE CRÉDITO', 'BANCO EN LINEA']
        #},      
        
        #'BBVA Bancomer':{
        #   'skiprows' : 7, 
        #    'usecols':'GQ:GR',
        #    'columns': ['CLIENTES BBVA BANCOMER', 'OTROS BANCOS']
        #},      

        #'Segmentación':{
        #   'skiprows' : 7, 
        #    'usecols':'GK:GN    ',
        #    'columns': ['Futbolero apasionado', 'Futbolero analítico', 'Futbolero social', 'Futbolero apático']
        #},     
        
        #'Apuestas Deportivas':{
        #   'skiprows' : 7, 
        #    'usecols':'HN:HO',
        #    'columns': ['SÍ', 'NO']
        #},     
        
        #'Caliente':{
        #   'skiprows' : 7, 
        #    'usecols':'HP:HQ',
        #    'columns': ['CONOCE', 'USA']
        #},      
}


}
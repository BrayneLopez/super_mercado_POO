from app.products.exceptionz.excp import (ProductActive, InvoiceCodes)

class ProductDateBase:
    def __init__(self):
        self.codes_eliminated = {12345678, 87654321}
        self.active_codes = {
    10203040,  50607080,  90102030,  14314502,  82773581,  
    33445566,  77889900,  12123434,  44556677,  
    88776655   
}
        self.stock =  {
            10203040: {
                'nombre': 'Leche Entera Colanta 1L',
                'precio': 4500,
                'vencimiento': '15/02/2026',
                'categoria': 'Lácteos'
            },
            50607080: {
                'nombre': 'Arroz Diana Premium 1kg',
                'precio': 3800,
                'vencimiento': '20/12/2026',
                'categoria': 'Granos'
            },
            90102030: {
                'nombre': 'Huevos AA x12',
                'precio': 8500,
                'vencimiento': '10/02/2026',
                'categoria': 'Proteína'
            },
            14314502: {
                'nombre': 'Pan Tajado Bimbo',
                'precio': 5200,
                'vencimiento': '01/01/2024', # PRODUCTO VENCIDO
                'categoria': 'Panadería'
            },
            82773581: {
                'nombre': 'Café Sello Rojo 500g',
                'precio': 16900,
                'vencimiento': '30/06/2027',
                'categoria': 'Despensa'
            },
            33445566: {
                'nombre': 'Aceite Girasol 1000ml',
                'precio': 12500,
                'vencimiento': '15/11/2026',
                'categoria': 'Aceites'
            },
            77889900: {
                'nombre': 'Pasta Doria Spaghetti',
                'precio': 2900,
                'vencimiento': '05/05/2027',
                'categoria': 'Pastas'
            },
            12123434: {
                'nombre': 'Atún Van Camp\'s Agua',
                'precio': 6400,
                'vencimiento': '10/10/2023', # PRODUCTO VENCIDO
                'categoria': 'Enlatados'
            },
            44556677: {
                'nombre': 'Detergente Ariel 1kg',
                'precio': 14200,
                'vencimiento': '01/01/2028',
                'categoria': 'Aseo'
            },
            88776655: {
                'nombre': 'Salchicha Ranchera x7',
                'precio': 9800,
                'vencimiento': '25/02/2026',
                'categoria': 'Cárnicos'
            }
}
     
    def product_active(self, code):
        if code in self.active_codes:
            raise ProductActive('INACTIVE_CODE','El codigo se euencntra en la Base Datos.')
        return True
        
    def factured_code(self, code): 
        if code in self.codes_eliminated:
            raise InvoiceCodes('PRODUCT_FACTURED','Producto facturado.')
        return True
    

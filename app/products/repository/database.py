from app.products.exceptions.excp import ProductActive, InvoiceCodes, ProductUnknowm
from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %I:%M %p")

class ProductDateBase:
    def __init__(self):
        self.codes_eliminated = {87654321}
        self.active_codes = {
    10203040,  50607080,  90102030,  14314502,  82773581,  
    33445566,  77889900,  12123434,  44556677,  
    88776655   
}
        self.stock = {
    '11/02/2026 02:12 PM': {
        10203040: {
            'nombre': 'Leche Entera Colanta 1L',
            'precio': 4500,
            'fecha de vencimiento': '15/02/2026',
            'categoria': 'Lácteos'
        }
    },
    '11/02/2026 02:14 PM': {
        50607080: {
            'nombre': 'Arroz Diana Premium 1kg',
            'precio': 3800,
            'fecha de vencimiento': '20/12/2026',
            'categoria': 'Granos'
        }
    },
    '11/02/2026 02:16 PM': {
        90102030: {
            'nombre': 'Huevos AA x12',
            'precio': 8500,
            'fecha de vencimiento': '10/02/2026',
            'categoria': 'Proteína'
        }
    },
    '11/02/2026 02:18 PM': {
        14314502: {
            'nombre': 'Pan Tajado Bimbo',
            'precio': 5200,
            'fecha de vencimiento': '01/01/2024',  # PRODUCTO VENCIDO
            'categoria': 'Panadería'
        }
    },
    '11/02/2026 02:20 PM': {
        82773581: {
            'nombre': 'Café Sello Rojo 500g',
            'precio': 16900,
            'fecha de vencimiento': '30/06/2027',
            'categoria': 'Despensa'
        }
    },
    '11/02/2026 02:22 PM': {
        33445566: {
            'nombre': 'Aceite Girasol 1000ml',
            'precio': 12500,
            'fecha de vencimiento': '15/11/2026',
            'categoria': 'Aceites'
        }
    },
    '11/02/2026 02:24 PM': {
        77889900: {
            'nombre': 'Pasta Doria Spaghetti',
            'precio': 2900,
            'fecha de vencimiento': '05/05/2027',
            'categoria': 'Pastas'
        }
    },
    '11/02/2026 02:26 PM': {
        12123434: {
            'nombre': "Atún Van Camp's Agua",
            'precio': 6400,
            'fecha de vencimiento': '10/10/2023',  # PRODUCTO VENCIDO
            'categoria': 'Enlatados'
        }
    },
    '11/02/2026 02:28 PM': {
        44556677: {
            'nombre': 'Detergente Ariel 1kg',
            'precio': 14200,
            'fecha de vencimiento': '01/01/2028',
            'categoria': 'Aseo'
        }
    },
    '11/02/2026 02:30 PM': {
        88776655: {
            'nombre': 'Salchicha Ranchera x7',
            'precio': 9800,
            'fecha de vencimiento': '25/02/2026',
            'categoria': 'Cárnicos'
        }
    }
}

     
    def product_active(self, code):
        if code in self.active_codes:
            raise ProductActive('INACTIVE_CODE','El codigo se encuentra Registrado.')
        
        
    def factured_code(self, code): 
        if code in self.codes_eliminated:
            raise InvoiceCodes('PRODUCT_FACTURED','Producto facturado.')
        
    
    def product_implementatio(self, code, new_product):
        self.stock.setdefault(time, {code:new_product})
        
    
    
    #// metodo de caja 
    def code_unknowm(self, code):
        if not all([self.product_active(code), self.factured_code(code)]):
            raise ProductUnknowm('PRODUCT_UNKNOWM', 'Producto Inexistente.')
        
    
    

        
        
        
        
    
        
        
    
        
    

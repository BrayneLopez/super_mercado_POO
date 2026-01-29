from datetime import datetime

time = datetime.now().strftime("%d/%m/%Y %I:%M %p")

class IncompleteLenght(Exception):
    def __init__(self, message_error, message):
        self.types_data_log = {
            'TYPE_ERROR_CODE':message_error,
            'MESSAGE':message,
            'RUNTIME':time
        }
        super().__init__(self.types_data_log)
        
class InvoiceCodes(Exception):
    def __init__(self, message_error, message):
        self.types_data_log = {
            'TYPE_ERROR_CODE':message_error,
            'MESSAGE':message,
            'RUNTIME':time
        }
        super().__init__(self.types_data_log)
             
class LimitedDateExpired(Exception):
    def __init__(self, message_error, message):
        self.types_data_log = {
            'TYPE_ERROR_CODE':message_error,
            'MESSAGE':message,
            'RUNTIME':time
        }
        super().__init__(self.types_data_log)     
         
class ProductActive(Exception):
    def __init__(self, message_error, message):
        self.types_data_log = {
            'TYPE_ERROR_CODE':message_error,
            'MESSAGE':message,
            'RUNTIME':time
        }
        super().__init__(self.types_data_log)

class PriceNotValue(Exception):
    def __init__(self, message_error, message):
        self.types_data_log = {
            'TYPE_ERROR_CODE':message_error,
            'MESSAGE':message,
            'RUNTIME':time
        }
        super().__init__(self.types_data_log)


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
        

class ValidationProductRegistration:
    def __init__(self, v, code, product, cost_payment, date_limited, category):
        self.v = v
        self.code = code
        self.product = product
        self.cost = cost_payment
        self.datelimited = date_limited
        self.category = category
        
        
    def code_format(self):
        if len(str(self.code)) != 8:
            raise IncompleteLenght('INCOMPLETE_LENGHT', 'Codigo con longitud inadecuada.')
        return True
        
    def product_active(self):
        if self.code in self.v.active_codes:
            raise ProductActive('INACTIVE_CODE','El codigo se euencntra en la Base Datos.')
        return True
    
    def date_in_range(self):
        if self.datelimited != '28/01/2026': # validacion de fecha del producto con fecha actual > aun no
            raise LimitedDateExpired('DATETIME_EXPIRED','Fecha Expirada.')
        return True
        
    def cost_zero(self):
        if self.cost == 0:
            raise PriceNotValue('PRICE_NOT_VALUE', 'Precio con valor 0')
        return True
    
    def factured_code(self):
        if self.code in self.v.codes_eliminated:
            raise InvoiceCodes('RPODUCT_FACTURED','Producto facturado.')
        return True
    
    def orquest(self):
        try:
            self.code_format()
            self.product_active()
            self.date_in_range()
            self.cost_zero()
            self.factured_code()
            
            
        except IncompleteLenght as e:
            return e.args[0]
        except ProductActive as e:
            return e.args[0]
        except LimitedDateExpired as e:
            return e.args[0]
        except PriceNotValue as e:
            return e.args[0]
        except InvoiceCodes as e:
            return e.args[0]
        

product_datebase = ProductDateBase() 
product = ValidationProductRegistration(product_datebase, 90102130, 'Gaseosa Manzana 2L', 4500, '28/01/2026', 'Bebida')
print(product.orquest())


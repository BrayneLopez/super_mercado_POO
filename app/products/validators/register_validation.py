from app.products.exceptions.excp import (
    IncompleteLenght, LimitedDateExpired,
    PriceNotValue, FortmatCodeNuemeric)


class ValidationProductRegistration:
    def __init__(self, db, code, product, cost_payment, date_limited, category):
        self.db = db
        self.code = code
        self.product = product
        self.cost = cost_payment
        self.datelimited = date_limited
        self.category = category
    
    def numeric_entry(self):#                           PENDING
        if not isinstance(self.code, int):
            raise FortmatCodeNuemeric('FORMAT_NOT_NUMERIC', 'Solo caracteres Numericos.')
       
        
        
    def code_format(self):
        if len(str(self.code)) != 8:
            raise IncompleteLenght('INCOMPLETE_LENGHT', 'longitud inadecuada.')
        
        
    
    def date_in_range(self):
        if self.datelimited != '28/01/2026': # validacion de fecha del producto con fecha actual > aun no
            raise LimitedDateExpired('DATE_EXPIRED','Fecha Expirada.')
        
        
    def cost_zero(self):
        if self.cost <= 0:
            raise PriceNotValue('PRICE_NOT_VALUE', 'Precio con valor 0')
        
    
    

        

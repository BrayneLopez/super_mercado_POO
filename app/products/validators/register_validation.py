from app.products.exceptionz.excp import (
    IncompleteLenght, InvoiceCodes, LimitedDateExpired, 
    ProductActive, PriceNotValue, ProductUnknowm)


class ValidationProductRegistration:
    def __init__(self, db, code, product, cost_payment, date_limited, category):
        self.db = db
        self.code = code
        self.product = product
        self.cost = cost_payment
        self.datelimited = date_limited
        self.category = category
        
        
    def code_format(self):
        if len(str(self.code)) != 8:
            raise IncompleteLenght('INCOMPLETE_LENGHT', 'longitud inadecuada.')
        return True
        
    
    def date_in_range(self):
        if self.datelimited != '28/01/2026': # validacion de fecha del producto con fecha actual > aun no
            raise LimitedDateExpired('DATE_EXPIRED','Fecha Expirada.')
        return True
        
    def cost_zero(self):
        if self.cost <= 0:
            raise PriceNotValue('PRICE_NOT_VALUE', 'Precio con valor 0')
        return True
    
    
    def orquest(self):
        try:
            self.code_format()
            self.db.product_active(self.code)
            self.date_in_range()
            self.cost_zero()
            self.db.factured_code(self.code)
            self.db.code_unknowm(self.code)
            
            
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
        except ProductUnknowm as e:
            return e.args[0]
        
        return {'nombre':self.product,
            'precio':self.cost, 
            'fecha de vencimiento':self.datelimited, 
            'categoria':self.category}
        

# clase single
from app.products.exceptionz.excp import (
    IncompleteLenght, InvoiceCodes, LimitedDateExpired, 
    ProductActive, PriceNotValue, ProductUnknowm)


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
        
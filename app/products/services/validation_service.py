# clase single
from app.products.exceptions.excp import (IncompleteLenght, InvoiceCodes, LimitedDateExpired,
                                        ProductActive, PriceNotValue, FortmatCodeNuemeric)

class OrquestValidationRaises:
    def __init__(self, numeric_entry, code_format, date_in_range, 
                 cost_zero, product_active, factured_code, code):
        
        self.numeric_entry = numeric_entry
        self.code_format = code_format
        self.date_in_range = date_in_range
        self.cost_zero = cost_zero
        self.product_active = product_active
        self.factured_code = factured_code
        self.code = code
        
        
    def orquest(self):
        self.numeric_entry()
        self.code_format()
        self.product_active(self.code)
        self.date_in_range()
        self.cost_zero()
        self.factured_code(self.code)
                #AGREGAR EN VALIDACION DE CAJA
            # self.db.code_unknowm(self.code)
   

class TypesOfErrors:
    def __init__(self, x):
        self.x = x
        
    def orchestra_validation(self):
        try:
            self.x.orquest()
        except FortmatCodeNuemeric as e:
            return e.args[0]
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
        

        return True
        

class AssigmentValidationCompletion:
    def __init__(self, a, category, product, cost, datelimited):
        self.a = a
        self.category = category
        self.product = product
        self.cost = cost
        self.datelimited = datelimited
        
        
    def validation_completion(self):

        if isinstance(self.a, bool):
            return {'nombre':self.product,'precio':self.cost, 
            'fecha de vencimiento':self.datelimited, 
            'categoria':self.category}
        else:
            return self.a
        

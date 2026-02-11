from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %I:%M %p")



class ExceptionStructure(Exception):
    def __init__(self, message_error, message):
        self.types_data_log = {
            'NAME_ERROR_CODE':message_error,
            'MESSAGE_TYPE_ERROR':message,
            'RUNTIME_AND_DATE':time
        }
        super().__init__(self.types_data_log)
    
    
class FortmatCodeNuemeric(ExceptionStructure):
    pass
class IncompleteLenght(ExceptionStructure):
    pass
class InvoiceCodes(ExceptionStructure):
    pass
class LimitedDateExpired(ExceptionStructure):     
    pass
class ProductActive(ExceptionStructure):
    pass
class PriceNotValue(ExceptionStructure):
    pass
class ProductUnknowm(ExceptionStructure):
    pass

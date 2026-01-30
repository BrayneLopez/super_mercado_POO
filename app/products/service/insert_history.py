from app.products.repository.log_data import LogDataBase
from app.products.repository.data_base import ProductDateBase
from app.products.validators.register_validation import ValidationProductRegistration

class ValidationProductsState:
    def __init__(self, log, db):
        self.log = log
        self.db = db
        
    def log_insert_validation(self, code, dicio):
        if 'nombre' in dicio:
            self.db.product_implementatio(code, dicio)
            self.log.process_ok(dicio)
            
        if 'NAME_ERROR_CODE' in dicio:
            self.log.procees_not_ok(dicio)
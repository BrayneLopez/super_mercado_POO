from app.products.repository.log_data import LogDataBase
from app.products.repository.data_base import ProductDateBase
from app.products.validators.register_validation import ValidationProductRegistration


class ValidationProductsState:
    def __init__(self, log, db, NAME_IN_KEY, NAME_ON_KEY_ERROR):
        self.NAME_IN_KEY = NAME_IN_KEY
        self.NAME_ON_KEY_ERROR = NAME_ON_KEY_ERROR
        self.log = log
        self.db = db
        
    def log_insert_validation(self, code, dicio):
        if self.NAME_IN_KEY.lower() in dicio:
            self.db.product_implementatio(code, dicio)
            self.log.process_ok(dicio)
            
        if self.NAME_ON_KEY_ERROR in dicio:
            self.log.procees_not_ok(dicio)
from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %I:%M %p")

from app.logs.process_log_product import LogDataBase
from app.products.repository.data_base import ProductDateBase
from app.products.validators.register_validation import ValidationProductRegistration
from app.products.service.insert_history import ValidationProductsState
from app.products.constants import NAME_IN_KEY, NAME_ON_KEY_ERROR
def run():
    log = LogDataBase()
    db = ProductDateBase()
    vp = ValidationProductsState(log, db, NAME_IN_KEY, NAME_ON_KEY_ERROR)
    register = ValidationProductRegistration(db, 12753958, 'Gaseosa Manzana 2L', 0, '28/01/2026', 'Bebida')
    
    new_product_implemented = register.orquest()
    vp.log_insert_validation(register.code, new_product_implemented)
    
    print(register.orquest())
    print(log.registration_successful)
    print(log.register_process_error)
    
if __name__ == "__main__":
    run()




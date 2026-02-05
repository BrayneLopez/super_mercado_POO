from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %I:%M %p")

from app.products.repository.log_data import LogDataBase
from app.products.repository.data_base import ProductDateBase
from app.products.validators.register_validation import ValidationProductRegistration
from app.products.service.insert_history import ValidationProductsState
from app.constants.product_const.assignment_key import NAME_IN_KEY, NAME_ON_KEY_ERROR
def run():
    log = LogDataBase()
    db = ProductDateBase()
    vn = ValidationProductsState(log, db, NAME_IN_KEY, NAME_ON_KEY_ERROR)
    register = ValidationProductRegistration(db, 1275358, 'Gaseosa Manzana 2L', 4500, '28/01/2026', 'Bebida')
    
    new_product_implemented = register.orquest()
    vn.log_insert_validation(register.code, new_product_implemented)
    
    print(register.orquest())
    print(log.registration_successful)
    print(log.register_process_error)
    
if __name__ == "__main__":
    run()




from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %I:%M %p")

from app.auth.login.repository.bd_register import LoginPortalProcess
from argon2 import PasswordHasher
from app.auth.login.validator.register_sesion import RegisterSesion
from app.auth.login.service.orquest import orquest_sesion_login # ejecuta validator
from app.auth.login.service.redirection import datas_ok

from app.logs.process_log_product import LogDataBase
from app.products.repository.database import ProductDateBase
from app.products.validators.register_validation import ValidationProductRegistration
from app.products.services.insert_history import ValidationProductsState
from app.products.services.validation_service import OrquestValidationRaises, TypesOfErrors, AssigmentValidationCompletion
from app.products.constants import NAME_IN_KEY, NAME_ON_KEY_ERROR


def register_prtoducts():
    
    log = LogDataBase()
    db = ProductDateBase()
    vlt = ValidationProductRegistration(db, 87654323, 'Gaseosa Manzana 2L', 1, '28/01/2026', 'Bebida')
    vps = ValidationProductsState(log, db, NAME_IN_KEY, NAME_ON_KEY_ERROR)
    orquest_exceptions = OrquestValidationRaises( vlt.numeric_entry, vlt.code_format, vlt.date_in_range, 
                                vlt.cost_zero, db.product_active, db.factured_code, vlt.code)
    caputary_errors = TypesOfErrors(orquest_exceptions)
    validation_ok = AssigmentValidationCompletion(caputary_errors.orchestra_validation(), vlt.category, vlt.product, vlt.cost, vlt.datelimited)
    
    data = validation_ok.validation_completion()
    vps.log_insert_validation(vlt.code, data)
    
    print(db.stock)
    print(log.registration_successful)
    print(log.register_process_error)
    

    
    
def post_registro_sesion():
    process_safe_private = PasswordHasher()
    a = LoginPortalProcess()
    x = RegisterSesion(a, process_safe_private, 'juan', '0324234242424', 'juanlopez@gmail.com') #se crea el objeto
    
    
     # lo pasamos para que se ejecute y nos devuleva un raise or dict
    z = datas_ok(a, orquest_sesion_login, x)
    a.x()
    
    
    
if __name__ == "__man__":
    register_prtoducts()

if __name__ == "__main__":
    post_registro_sesion()



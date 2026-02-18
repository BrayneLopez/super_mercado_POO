from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %I:%M %p")

from app.logs.process_log_product import LogDataBase
from app.products.repository.database import ProductDateBase
from app.products.validators.register_validation import ValidationProductRegistration
from app.products.services.insert_history import ValidationProductsState
from app.products.services.validation_service import OrquestValidationRaises, TypesOfErrors, AssigmentValidationCompletion
from app.products.constants import NAME_IN_KEY, NAME_ON_KEY_ERROR


def run():
    
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
    
if __name__ == "__main__":
    run()




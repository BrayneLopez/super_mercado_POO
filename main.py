
from app.products.repository.data_base import ProductDateBase
from app.products.validators.register import ValidationProductRegistration


def run():
    db = ProductDateBase()
    
    register = ValidationProductRegistration(db, 12345678, 'Gaseosa Manzana 2L', 4500, '28/01/2026', 'Bebida')
    print(register.orquest())
    

if __name__ == "__main__":
    run()





from datetime import datetime       


class LoginPortalProcess:
    def __init__(self):
        self.time = datetime.now().strftime('%d-%m-%y %I:%M: %p')
        self.register_uuid_date = {}
        self.user_data_save = {}
        self.pair_of_unknown_data = {}
    
        self.one = None
        self.two = None
        self.three = None
        #UPDATE DICT DATA 
    def date_register_user_log(self, one): #// REDIRIGE EL UUID + FECHA DE CREACION DE UNA CUENTA
        self.register_uuid_date = one

    def sending_user_data(self, two): #// ENVIA LOS DATOS A BD
        self.user_data_save = two 

    def linked_data_redirection(self, three): #// ENVIA HASH + UUID A BD 
        self.pair_of_unknown_data = three
        
        
        #DATA VALIDATION IN DICT
        
    def format_validation(self, data_save):
        if all(self.data_save.key() in data_save):
            pass
    def uuid_duplicate(self, two):  #UUID NOT DUPLICATE
        if not two.key() in self.register_uuid_date:
            raise #DATA DUPLICATE
        else:
            self.one =  None
    
        if all([]):
            pass
    
    def unknown_data_together(self): # CONTRASENA HASEADA OK
        pass

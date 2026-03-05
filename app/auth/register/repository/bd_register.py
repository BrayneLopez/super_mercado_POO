
from datetime import datetime       

class LoginPortalProcess:
    def __init__(self):
        self.time = datetime.now().strftime('%d-%m-%y %I:%M: %p')
        self.register_uuid_date = {}
        self.user_data_save = {}
        self.pair_of_unknown_data = {}
    
        
        #UPDATE DICT DATA 
    def date_register_user_log(self, one): #// REDIRIGE EL UUID + FECHA DE CREACION DE UNA CUENTA
        self.register_uuid_date = one

    def sending_user_data(self, two): #// ENVIA LOS DATOS A BD
        self.user_data_save = two 

    def linked_data_redirection(self, three): #// ENVIA HASH + UUID A BD 
        self.pair_of_unknown_data = three
        
    def x(self):
        print(self.register_uuid_date)
        print(self.user_data_save)
        print(self.pair_of_unknown_data)
        #DATA VALIDATION IN DICT
        

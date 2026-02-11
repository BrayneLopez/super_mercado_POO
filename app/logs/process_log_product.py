from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %I:%M %p")

class LogDataBase:
    def __init__(self):
        self.registration_successful = {}
        self.register_process_error = {}
    
    def process_ok(self, code, data): #    AGREGA LOG SI EL DICC ES DEL PRODUCTO
        self.registration_successful.setdefault(time, {code:data})
    
    def procees_not_ok(self, code, data):#    AGREGA LOG SI SALE UN ERROR
        self.register_process_error.setdefault(time, {code:data})
        
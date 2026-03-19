from datetime import datetime

time = datetime.now().strftime('%d-%m-%y %I:%M')

class LoginRais(Exception):
    def __init__(self, error_name, error_message):
        types_errors_logins = {
            'NAME_TYPE_ERROR':error_name,
            'MESSAGE':error_message,
            'RUNTIME':time
        }
        super().__init__(types_errors_logins)
        

class EmailNotFormat(LoginRais):
    pass
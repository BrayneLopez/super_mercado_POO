from datetime import datetime
time = datetime.now().strftime('%d/%m/%y %I:%M %p')

class FormatTypesLogs(Exception):
    def __init__(self, TYPES_ERROR, MESSAGE, CODES):
        self.log_login_sesion = {
            'NAME_TYPE_ERROR':TYPES_ERROR,
            'MESSAGE':MESSAGE,
            "TYPE_ERROR_CODE":CODES,
            'RUNTIME_DATE':time
        }
        super().__init__()
        

class FormatTextUsername(FormatTypesLogs):
    pass
class Usernamelength(FormatTypesLogs):
    pass
class PasswordLength(FormatTypesLogs):
    pass
class PasswordBannedOn(FormatTypesLogs):
    pass
class SafeFormatHashe(FormatTypesLogs):
    pass
class EmailFormatOk(FormatTypesLogs):
    pass
class EmailDomineOn(FormatTypesLogs):
    pass

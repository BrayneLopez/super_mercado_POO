
from app.auth.login.repository.raises_login import (FormatTextUsername, Usernamelength, PasswordLength, PasswordBannedOn, 
SafeFormatHashe,SpaceEmailOn, EmailFormatOk, EmailDomineOn)


def datas_ok(prueba, orquest_sesion_login, x):
    try:
        a = orquest_sesion_login(x)
    except (FormatTextUsername, Usernamelength, PasswordLength, PasswordBannedOn,
            SafeFormatHashe, SpaceEmailOn, EmailFormatOk, EmailDomineOn) as e:
        return e.args[0]

    else:  
        prueba.date_register_user_log(a[0]) #// REDIRIGE EL UUID + FECHA DE CREACION DE UNA CUENTA
        prueba.sending_user_data(a[1])   #// ENVIA LOS DATOS A BD
        prueba.linked_data_redirection(a[2])   #// ENVIA HASH + UUID A BD 
    

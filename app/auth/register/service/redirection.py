
from app.auth.register.repository.raises_login import (FormatTextUsername, Usernamelength, PasswordLength, PasswordBannedOn, 
SafeFormatHashe,SpaceEmailOn, EmailFormatOk, EmailDomineOn)


def datas_ok(assignment_guide, orquest_sesion_login, root_process):
    try:
        process_residue = orquest_sesion_login(root_process)
    except (FormatTextUsername, Usernamelength, PasswordLength, PasswordBannedOn,
            SafeFormatHashe, SpaceEmailOn, EmailFormatOk, EmailDomineOn) as e:
        return e.log_login_sesion
    
    else:
        if 'OK' in process_residue:
            UNPAKING = process_residue.get('OK')
            assignment_guide.date_register_user_log(UNPAKING.get('DATA_LOG')) #// REDIRIGE EL UUID + FECHA DE CREACION DE UNA CUENTA
            assignment_guide.sending_user_data(UNPAKING.get('USER_PROFILE_DATA'))   #// ENVIA LOS DATOS A BD
            assignment_guide.linked_data_redirection(UNPAKING.get('HASHED_PASSWORD'))   #// ENVIA HASH + UUID A BD]
        
        #raise = DATA_FORMAT_FAILED data mal formado 500


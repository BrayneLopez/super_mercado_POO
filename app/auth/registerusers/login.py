from argon2 import PasswordHasher
from datetime import datetime
import uuid
from raises_login import (FormatTextUsername, Usernamelength, PasswordLength, 
PasswordBannedOn, SafeFormatHashe, EmailFormatOk, EmailDomineOn)
from registerusers.process_login import LoginPortalProcess


process_safe_private = PasswordHasher()
obj = LoginPortalProcess()


class RegisterSesion:
    def __init__(self, obj, process_safe_private, username, password, email):
        self.time = datetime.now().strftime('%d-%m-%y %I:%M: %p')
        self.obj = obj
        self.id_username = str(uuid.uuid4())
        self.process_safe_private = process_safe_private
        self.unknwom = None
        
        self.username = username
        self.password = password
        self.email = email
    
    #// CLEAN INPUT 
    def clean_format_inputs(self):
        self.username = self.username.strip()
        self.email = self.email.strip()
        self.password = self.password.strip()
    
    #// USERNAME
    
    def username_text_format(self):
        if not self.username.isalpha():
            raise FormatTextUsername('FORMAT_INVALIDE', 'Formato invalido', 400)
            
    def username_length(self):
        if len(self.username) > 12:
            raise Usernamelength('NAME_MAXIMUM_CHARACTERS', 'El nombre debe tener Maximo 12 Caracteres.', 400)
        
    
    #// PASSWORD
    def space_format(self):
         if ' ' in self.password:  # espacio en password
            pass
    
    def password_lenght(self):
        if not len(self.password) >= 12:
            raise PasswordLength('INSUFFICIENT_LENGTH', 'La contrasena debe tener minimo 12 Caracteres.', 400)
        
    def password_banned(self):
        if self.password in {
    "123456789012",
    "abcdefghijklm",
    "password123456",
    "passwordpassword",
    "qwertyuiopasdfg",
    "administrador123",
    "micasamicasa123",
    "colombiacolombia",
    "contraseñasegura123",
    "nomascontraseñas",
    "Iloveyou1234567",
    "aaaaaaaaaaaaaa",
    "11111111111111",
    "pablopablopablo",
    "supermarket2026",
    "secretpassword123",
    "0000000000",
    "admin1234567"
}:
            raise PasswordBannedOn('NOT_SAFE_PASSWORD', 'Selecciona una contraseña mas segura.Intenta mezclar letras, numeros y simbolos.', 400)
        else:
            self.unknwom = process_safe_private.hash(self.password)
    
    def safe_password_format(self):
        if not isinstance(self.unknwom, str) and self.unknwom.startwith('$argon2'):
           raise SafeFormatHashe('PROCESS_NOT_OK_HARSHER', 'FAILED_HASH', 500) 
    
    
    #// EMAIL   -   VALIDATION BASIC
    def email_format_ok(self):
        if not self.email.count('@') == 1 and self.email.count('.') == 1:
            raise EmailFormatOk('FORMAT_INVALIDE_EMAIL', 'Formato incorrecto. usa algo como ejemplo123@gmail.com', 400)
      
    
    def email_domain_ok(self):
        if not self.email.endswith(('.com', '.net', '.gov', '.hotmail')):
            raise EmailDomineOn('DOMAIN_NOT_OK', 'Dominio Ivalido', 400)
        else:
            self.obj.date_register_user_log({self.id_username:self.time})
            self.obj.sending_user_data({self.id_username:{'name':self.username,'email':self.email,'role':None,'datetimming':self.time}})
            self.obj.linked_data_redirection({self.id_username:self.unknwom})
            
    
    
x = RegisterSesion(obj, process_safe_private, 'juan', '3145200345Rm00', 'juanlopez@gmail.com')
    
def orquest_sesion_login():
    x.clean_format_inputs()
    x.username_text_format()
    x.username_length()
    x.password_lenght()
    x.password_banned()
    x.safe_password_format()
    x.email_format_ok()
    x.email_domain_ok()
    
response_register = orquest_sesion_login()

print(obj.register_uuid_date)
print(obj.user_data_save)
print(obj.pair_of_unknown_data)

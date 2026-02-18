
from raises import FormatNameError

class UsersLogin:
    def __init__(self, username, password, email):
    
        self.username = username
        self.password = password
        self.emaill = email
        
    def username_format(self):
        if not self.username.isalpha():
            print('SOLO LETRAS')
            
            #raise ValueError('Solo Puedes ingresar Letras.') # ejemeplo
        
    def username_length(self):
        if len(self.username) > 12:
            raise FormatNameError('FORMAT_NAME_ERROR', 'El nombre debe tener maximos 12 Letras.')
        
    
    def password_lenght(self):
        if not len(self.password) >= 12:
            print('LA CONTRASENA DEBE TENER MINIMO 12 CARACTERES')
        return {self.username:self.password}
    
    def safe_characters_password(self):
        if self.password:
            pass
        
    def email_format_ok(self):
        pass
    
    def email_domain_ok(self):
        pass
    

x = UsersLogin('lucassssssssssssss', None, None)


try:
    x.username_length()
except FormatNameError as e:
    print(e.args[0])

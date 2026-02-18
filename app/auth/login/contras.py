from argon2 import PasswordHasher

psh = PasswordHasher()

x = input('Contra:')
print(psh.hash(x))
print(psh.verify('1234', x))
    

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated ='auto')

class Hash():
   # To encrypt the password
   def bcrypt(password:str):
      return pwd_context.hash(password)

   # To decrypt the password
   def verify(plain_password, hashed_password ):
      return pwd_context.verify(plain_password,hashed_password )

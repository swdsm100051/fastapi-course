from pydantic import BaseModel

class AdminLogin(BaseModel):
   username: str
   password: str

   class Config():
      orm_mode = True
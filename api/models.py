from sqlalchemy import String, Integer, Column

from .database import Base


class AdminLogin(Base):
   __tablename__ = "admin"

   id = Column(Integer, primary_key=True, index= True)
   username = Column(String(50), nullable=False, unique= True)
   password = Column(String(255), nullable=False)

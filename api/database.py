import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load env config
load_dotenv()

# Config
HOST = os.environ.get('HOST')
HOST_USER = os.environ.get('HOST_USER')
HOST_PASSWORD = os.environ.get('HOST_PASSWORD')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

SQLALCHEMY_DATABASE_URL = f"postgresql://{HOST_USER}:{HOST_PASSWORD}@{HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Get database up 
def get_db():
   db = SessionLocal()
   try:
      yield db;
   finally:
      db.close()
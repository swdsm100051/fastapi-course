import os
from fastapi import FastAPI
import os
from dotenv import load_dotenv

from .routers import admin
from . import models
from .database import engine


app = FastAPI()

models.Base.metadata.create_all(bind= engine)


# Load Environment Variables
load_dotenv()

# Admin Routes
app.include_router(admin.router)


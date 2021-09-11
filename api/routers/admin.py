from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from .. import models
from ..schemas import AdminLogin
from ..database import get_db
from ..hashing import Hash


router = APIRouter(
    prefix='/admin',
    tags=['Admin']
)

@router.post("")
def login(request: AdminLogin, db: Session = Depends(get_db)):
    user = db.query(models.AdminLogin).filter(request.username == models.AdminLogin.username).first()
    # Checking the user
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, error= "Invalid Credentials")

    # Verifying the password
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, error="Password is incorrect")

    # Generate JWT token and return it
    return user
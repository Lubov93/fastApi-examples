from fastapi import APIRouter, Depends
from shemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create user
@router.post('/', response_model=UserDisplay) # For issues look in shemas.py
def create_user(request: UserBase,
                db: Session = Depends(get_db)):  # Depends of in database.py function get_db which MAIN SETTING OF DB
    return db_user.create_user(db, request)

# Read user

# Update user

# Delete user

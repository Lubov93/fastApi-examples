from typing import List
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

# Read all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read one user
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db:Session = Depends(get_db)):
    return db_user.get_user(db, id)


# Update user

# Delete user

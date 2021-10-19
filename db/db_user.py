from sqlalchemy.orm.session import Session
from shemas import UserBase
from db.models import DbUser


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )  # from models.py look
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh because id reason for new_user
    return new_user

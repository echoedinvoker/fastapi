from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.routing import request_response

from db.database import get_db
from db import db_user
from schemas import UserBase, UserDisplay


router = APIRouter(
        prefix='/user',
        tags=['user']
        )

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read all users
#@router.get('/', response_model=List[UserDisplay])
@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    result = db_user.get_all_users(db)
    print(result)
    return result

# Read one user
@router.get('/{id}', response_model=UserDisplay | None)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# Update user
@router.put('/{id}')
def Update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)

# Delete user
@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)


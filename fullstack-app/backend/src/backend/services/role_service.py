from sqlmodel import Session
from src.backend.repositories import role_repo
from src.backend.dto.role_dto import RoleCreate
from fastapi import HTTPException

def add_new_role(db: Session, role_data: RoleCreate):
    if role_data.name == "":
        raise HTTPException(status_code=400, detail="Nama role ga boleh kosong!")
    return role_repo.create_role(db, role_data)
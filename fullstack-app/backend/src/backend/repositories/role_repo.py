from sqlmodel import Session, select
from src.backend.database.schema.models import Role
from src.backend.dto.role_dto import RoleCreate, RoleResponse

def create_role(db: Session, role_create: RoleCreate):
    new_role = Role(name=role_create.name, description=role_create.description)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_roles(db: Session):
    return db.exec(select(Role)).all()
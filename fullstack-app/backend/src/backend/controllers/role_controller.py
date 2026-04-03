from sqlmodel import Session
from src.backend.services import role_service
from src.backend.dto.role_dto import RoleCreate

def create_role_controller(role: RoleCreate, db: Session):
    # Langsung lempar ke service
    return role_service.add_new_role(db, role)
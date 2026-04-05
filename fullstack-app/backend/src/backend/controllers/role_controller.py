from sqlmodel import Session
from src.backend.services import role_service
from src.backend.dto.role_dto import RoleCreate

# 1. CREATE
def create_role_controller(role: RoleCreate, db: Session):
    return role_service.add_new_role(db, role)

# 2. READ ALL
def get_all_roles_controller(db: Session):
    return role_service.get_all_roles(db)

# 3. READ BY ID
def get_role_by_id_controller(role_id: int, db: Session):
    return role_service.get_role(db, role_id)

# 4. UPDATE
def update_role_controller(role_id: int, role: RoleCreate, db: Session):
    return role_service.modify_role(db, role_id, role)

# 5. DELETE
def delete_role_controller(role_id: int, db: Session):
    return role_service.remove_role(db, role_id)
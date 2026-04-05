from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.database.connection import get_session
from src.backend.dto.role_dto import RoleCreate, RoleResponse
from src.backend.controllers import role_controller

router = APIRouter(prefix="/roles", tags=["Roles"])

# 1. CREATE (POST)
@router.post("/", response_model=RoleResponse, status_code=201)
def create_role_route(role: RoleCreate, db: Session = Depends(get_session)):
    return role_controller.create_role_controller(role, db)

# 2. READ ALL (GET)
@router.get("/", response_model=list[RoleResponse])
def get_all_roles_route(db: Session = Depends(get_session)):
    return role_controller.get_all_roles_controller(db)

# 3. READ BY ID (GET)
@router.get("/{role_id}", response_model=RoleResponse)
def get_role_by_id_route(role_id: int, db: Session = Depends(get_session)):
    return role_controller.get_role_by_id_controller(role_id, db)

# 4. UPDATE (PUT)
@router.put("/{role_id}", response_model=RoleResponse)
def update_role_route(role_id: int, role: RoleCreate, db: Session = Depends(get_session)):
    return role_controller.update_role_controller(role_id, role, db)

# 5. DELETE (DELETE)
@router.delete("/{role_id}")
def delete_role_route(role_id: int, db: Session = Depends(get_session)):
    return role_controller.delete_role_controller(role_id, db)
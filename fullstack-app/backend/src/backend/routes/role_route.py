from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.database.connection import get_session
from src.backend.dto.role_dto import RoleCreate, RoleResponse
from src.backend.controllers import role_controller

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RoleResponse, status_code=201)
def create_role_route(role: RoleCreate, db: Session = Depends(get_session)):
    # Manggil controller
    return role_controller.create_role_controller(role, db)

# @router.get("/")
# def get_all_roles(db: Session = Depends(get_session)):
#     # Panggil fungsi repo langsung atau lewat service
#     pass
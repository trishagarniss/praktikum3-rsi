from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.database.connection import get_session
from src.backend.dto.registration_dto import RegistrationCreate, RegistrationResponse
from src.backend.controllers import registration_controller
from src.backend.utils.security import require_user, require_admin

router = APIRouter(prefix="/registrations", tags=["Registrations"])

# 1. CREATE (POST) - User bisa mendaftar
@router.post("/", response_model=RegistrationResponse, status_code=201)
def create_registration_route(
    registration: RegistrationCreate, 
    db: Session = Depends(get_session),
    user_payload: dict = Depends(require_user)
):
    return registration_controller.create_registration_controller(registration, db)

# 2. READ ALL (GET) - User bisa melihat data
@router.get("/", response_model=list[RegistrationResponse])
def get_all_registrations_route(
    db: Session = Depends(get_session),
    user_payload: dict = Depends(require_user)
):
    return registration_controller.get_all_registrations_controller(db)

# 3. READ BY ID (GET) - User bisa melihat data
@router.get("/{registration_id}", response_model=RegistrationResponse)
def get_registration_by_id_route(
    registration_id: int, 
    db: Session = Depends(get_session),
    user_payload: dict = Depends(require_user)
):
    return registration_controller.get_registration_by_id_controller(registration_id, db)

# 4. UPDATE (PUT) - Hanya Admin yang bisa mengubah
@router.put("/{registration_id}", response_model=RegistrationResponse)
def update_registration_route(
    registration_id: int, 
    registration: RegistrationCreate, 
    db: Session = Depends(get_session),
    admin_payload: dict = Depends(require_admin)
):
    return registration_controller.update_registration_controller(registration_id, registration, db)

# 5. DELETE (DELETE) - Hanya Admin yang bisa menghapus
@router.delete("/{registration_id}")
def delete_registration_route(
    registration_id: int, 
    db: Session = Depends(get_session),
    admin_payload: dict = Depends(require_admin)
):
    return registration_controller.delete_registration_controller(registration_id, db)
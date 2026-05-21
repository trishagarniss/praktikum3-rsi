from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.database.connection import get_session
from src.backend.dto.event_dto import EventCreate, EventUpdate, EventResponse
from src.backend.controllers import event_controller
from src.backend.utils.security import require_admin

router = APIRouter(prefix="/events", tags=["Events"])

# 1. CREATE - HANYA ADMIN (POST)
@router.post("/", response_model=EventResponse, status_code=201)
def create_event_route(
    event: EventCreate, 
    db: Session = Depends(get_session),
    admin_payload: dict = Depends(require_admin)
):
    return event_controller.create_event_controller(event, db)

# 2. READ ALL - PUBLIK (GET)
@router.get("/", response_model=list[EventResponse]) 
def get_all_events_route(
    db: Session = Depends(get_session),
):
    return event_controller.get_all_events_controller(db)

# 3. READ ALL - KHUSUS ADMIN (GET)
@router.get("/admin", response_model=list[EventResponse])
def get_all_events_admin_route(
    db: Session = Depends(get_session),
    admin_payload: dict = Depends(require_admin)
):
    return event_controller.get_all_events_controller(db)

# 4. READ BY ID - PUBLIK (GET)
@router.get("/{event_id}", response_model=EventResponse)
def get_event_by_id_route(
    event_id: int, 
    db: Session = Depends(get_session),
):
    return event_controller.get_event_by_id_controller(event_id, db)

# 5. UPDATE - HANYA ADMIN (PUT)
@router.put("/{event_id}", response_model=EventResponse)
def update_event_route(
    event_id: int, 
    event: EventUpdate, 
    db: Session = Depends(get_session),
    admin_payload: dict = Depends(require_admin)
):
    return event_controller.update_event_controller(event_id, event, db)    

# 6. DELETE - HANYA ADMIN (DELETE)
@router.delete("/{event_id}")
def delete_event_route(
    event_id: int, 
    db: Session = Depends(get_session),
    admin_payload: dict = Depends(require_admin) 
):
    return event_controller.delete_event_controller(event_id, db)
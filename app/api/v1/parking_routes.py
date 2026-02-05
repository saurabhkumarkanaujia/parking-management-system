from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.session import SessionLocal
from app.schemas.parking import (
    ParkingSpaceResponse,
    ParkingExitRequest
)
from app.repositories.parking_repository import ParkingRepository
from app.services.parking_service import ParkingService

router = APIRouter(prefix="/parking-spaces", tags=["Parking"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=List[ParkingSpaceResponse])
def get_all(db: Session = Depends(get_db)):
    return ParkingRepository.get_all(db)


@router.get("/empty", response_model=List[ParkingSpaceResponse])
def get_empty(db: Session = Depends(get_db)):
    return ParkingRepository.get_empty(db)


@router.get("/empty/{level}", response_model=List[ParkingSpaceResponse])
def get_empty_by_level(level: int, db: Session = Depends(get_db)):
    return ParkingRepository.get_empty_by_level(db, level)


@router.post("/exit")
def exit_parking(data: ParkingExitRequest, db: Session = Depends(get_db)):
    space = ParkingRepository.mark_exit(
        db, data.level, data.spot_number
    )
    if not space:
        return {"message": "Parking space not found"}
    return {"message": "Parking space released"}


@router.get("/full-capacity")
def full_capacity(db: Session = Depends(get_db)):
    return {"is_full": ParkingService.is_full(db)}

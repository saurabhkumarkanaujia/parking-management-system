from sqlalchemy.orm import Session
from app.repositories.parking_repository import ParkingRepository

class ParkingService:

    @staticmethod
    def is_full(db: Session):
        return ParkingRepository.empty_count(db) == 0

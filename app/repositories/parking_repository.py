from sqlalchemy.orm import Session
from app.models.parking_space import ParkingSpace

class ParkingRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(ParkingSpace).all()

    @staticmethod
    def get_empty(db: Session):
        return db.query(ParkingSpace).filter(
            ParkingSpace.is_available == True
        ).all()

    @staticmethod
    def get_empty_by_level(db: Session, level: int):
        return db.query(ParkingSpace).filter(
            ParkingSpace.level == level,
            ParkingSpace.is_available == True
        ).all()

    @staticmethod
    def mark_exit(db: Session, level: int, spot_number: int):
        space = db.query(ParkingSpace).filter_by(
            level=level,
            spot_number=spot_number
        ).first()

        if space:
            space.is_available = True
            space.license_plate = None
            db.commit()

        return space

    @staticmethod
    def empty_count(db: Session):
        return db.query(ParkingSpace).filter(
            ParkingSpace.is_available == True
        ).count()

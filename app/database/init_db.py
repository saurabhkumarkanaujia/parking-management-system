from app.database.session import engine
from app.database.base import Base
from app.models.parking_space import ParkingSpace

def init_db():
    Base.metadata.create_all(bind=engine)

    from sqlalchemy.orm import Session
    db = Session(bind=engine)

    for level in range(1, 4):
        for spot in range(1, 11):
            exists = db.query(ParkingSpace).filter_by(
                level=level, spot_number=spot
            ).first()
            if not exists:
                db.add(ParkingSpace(level=level, spot_number=spot))

    db.commit()
    db.close()

from sqlalchemy import Column, Integer, Boolean, String
from app.database.base import Base

class ParkingSpace(Base):
    __tablename__ = "parking_spaces"

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, index=True)
    spot_number = Column(Integer)
    is_available = Column(Boolean, default=True)
    license_plate = Column(String, nullable=True)

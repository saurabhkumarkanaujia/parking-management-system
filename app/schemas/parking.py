from pydantic import BaseModel
from typing import Optional

class ParkingSpaceResponse(BaseModel):
    id: int
    level: int
    spot_number: int
    is_available: bool
    license_plate: Optional[str]

    class Config:
        orm_mode = True


class ParkingExitRequest(BaseModel):
    level: int
    spot_number: int

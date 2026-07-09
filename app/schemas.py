from pydantic import BaseModel, Field
from random import randint
from enum import Enum

def random_destination():
    return randint(11000, 11999)

class Shipment(BaseModel):
    content: str = Field(description="content of shipment",max_length=30)
    weight: float = Field(description="weight of the shipment in kgs",le=25, ge=1)
    destination: int | None = Field(description="Destination zipcode",default_factory=random_destination)

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int

class ShipmentRead(BaseShipment):
    status: ShipmentStatus

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    content: str | None = Field(default=None)
    weight: float | None = Field(default=None, le=25)
    destination: int | None = Field(default=None)
    status: ShipmentStatus
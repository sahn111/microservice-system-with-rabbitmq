# type: ignore
from typing import Any, Dict
from sqlalchemy import Column, String, DateTime
from datetime import datetime

from .base import Base

import json

JSONObject = Dict[str, Any]


class Device(Base):
    __tablename__ = "device"
    __table_args__ = {"schema": "public"}

    device_id: str = Column(String, primary_key=True)
    device_name: str = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())

    def __str__(self) -> str:
        return json.dumps(self.dict())

    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class Location(Base):
    __tablename__ = "location"
    __table_args__ = {"schema": "public"}

    location_id: str = Column(String, primary_key=True)
    device_id: str = Column(String)
    x_coordinate: str = Column(String)
    y_coordinate: str = Column(String)
    create_date: datetime = Column(DateTime)

    def __repr__(self) -> str:
        return json.dumps(self.dict())

    def __str__(self) -> str:
        return json.dumps(self.dict())

    def dict(self) -> dict:
        return OrmHelper.toDict(self)

import json
from typing import Literal
from pydantic import BaseModel

class DeviceLocation(BaseModel):
    device_id : str
    x_coordinate: str
    y_coordinate: str

    def __json__(self):
        return json.dumps(self)

class SystemLogPydantic(BaseModel):
    type: Literal["INFO", "WARNING", "CRITICAL", "ERROR"]
    message: str

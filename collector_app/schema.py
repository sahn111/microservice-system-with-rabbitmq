import json

from pydantic import BaseModel
class DeviceLocation(BaseModel):
    device_id : str
    x_coordinate: str
    y_coordinate: str

    def __json__(self):
        return json.dumps(self)
    
class CreateDeviceModel(BaseModel):
    device_name : str
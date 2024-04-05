from ....schema import CreateDeviceModel
from ....db.db_session_middleware import db_session_middleware
from ....db.models import Device
from sqlalchemy.sql import insert
from uuid import uuid4

def create_device_repository(data : CreateDeviceModel, db_session : db_session_middleware):
    device_create_query = insert(Device).values(
        device_id = uuid4(),
        device_name = data.device_name
    )
    db_session.execute(device_create_query)
    db_session.commit() 

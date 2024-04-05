from ....schema import CreateDeviceModel
from ....db.db_session_middleware import db_session_middleware
from ....db.models import Device
from sqlalchemy.sql import select

def get_device_repository(device_id : str, db_session : db_session_middleware):
    get_device_query = select(Device).where(Device.device_id == device_id)
    db_session.execute(get_device_query)
    db_session.commit() 
    return 200
from ....schema import CreateDeviceModel
from ....db.db_session_middleware import db_session_middleware
from ....db.models import Device
from sqlalchemy.sql import select

def get_all_devices_repository(db_session : db_session_middleware):
    get_all_devices_query = select(Device)
    db_session.execute(get_all_devices_query)
    db_session.commit() 
    return 200

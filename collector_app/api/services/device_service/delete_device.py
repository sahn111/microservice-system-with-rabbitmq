from ....schema import CreateDeviceModel
from ...repositories import *
from ....db.db_session_middleware import db_session_middleware

def delete_device_service(device_id : str, db_session : db_session_middleware):
    ...
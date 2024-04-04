from ....schema import CreateDeviceModel
from ...repositories import *
from ....db.db_session_middleware import db_session_middleware

def create_device_service(data : CreateDeviceModel, db_session : db_session_middleware):
    ...
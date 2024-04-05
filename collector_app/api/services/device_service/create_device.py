from ....schema import CreateDeviceModel
from ...repositories import create_device_repository
from ....db.db_session_middleware import db_session_middleware

def create_device_service(data : CreateDeviceModel, db_session : db_session_middleware):
    create_device_repository(data=data, db_session=db_session)
    return 200
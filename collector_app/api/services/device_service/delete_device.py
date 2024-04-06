from ...repositories import delete_device_repository
from ....db.db_session_middleware import db_session_middleware

def delete_device_service(device_id : str, db_session : db_session_middleware):
    delete_device_repository(device_id=device_id, db_session=db_session)
    return 200
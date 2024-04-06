from ...repositories import get_all_devices_repository, get_device_repository
from ....db.db_session_middleware import db_session_middleware

def get_device_service(db_session : db_session_middleware, device_id = None):

    if device_id:
        # Get specific device
        return get_device_repository(device_id=device_id, db_session=db_session)
    else:
        # Get all devices
        return get_all_devices_repository(db_session=db_session)
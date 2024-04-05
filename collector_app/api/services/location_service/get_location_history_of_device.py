from ....schema import CreateDeviceModel
from ...repositories import *
from ....db.db_session_middleware import db_session_middleware

def get_location_history_of_device_service(db_session : db_session_middleware, device_id = None):

    if device_id:
        # Get specific device's location history
        ...
    else:
        # Get all devices' location history
        ...
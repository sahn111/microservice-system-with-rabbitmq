from ...repositories import *
from ....db.db_session_middleware import db_session_middleware

def get_last_location_of_device_service(db_session : db_session_middleware, device_id = None):

    locations_of_device = get_locations_of_device_repository(device_id = device_id, db_session=db_session, get_last=True)
    return locations_of_device
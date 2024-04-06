from ...repositories import get_locations_of_device_repository
from ....db.db_session_middleware import db_session_middleware

def get_location_history_of_device_service(db_session : db_session_middleware, device_id = None):

    locations_of_device = get_locations_of_device_repository(device_id = device_id, db_session=db_session)
    return locations_of_device
from ....schema import CreateDeviceModel
from ....db.db_session_middleware import db_session_middleware
from ....db.models import Location
from sqlalchemy.sql import select

def get_location_repository(db_session : db_session_middleware):
    ...
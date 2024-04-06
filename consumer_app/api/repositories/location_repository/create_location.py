from ....db.db_session_middleware import db_session_middleware
from ....db.models import Location
from ....schema import DeviceLocation, SystemLogPydantic
from ....log_service import write_system_logging_message

from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import insert

def create_location_repository(data : DeviceLocation, db_session : db_session_middleware):
    location_create_query = insert(Location).values(
        location_id = uuid4(),
        device_id = data.device_id,
        x_coordinate = data.x_coordinate,
        y_coordinate = data.y_coordinate,
        create_date = datetime.now() 
    )
    db_session.execute(location_create_query)
    db_session.commit() 
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Create location {data.device_id} is completed successfully"
        )
    )
    return 200
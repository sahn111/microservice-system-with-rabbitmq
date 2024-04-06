from ...repositories import create_location_repository
from ....db.db_session_middleware import db_session_middleware
from fastapi import Depends
import json
from ....schema import DeviceLocation, SystemLogPydantic
from ....log_service import write_system_logging_message

def create_location_service(data):
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Create location {data} is started"
        )
    )
    db_session = db_session_middleware()
    # Manipulate raw data
    raw_data = data.decode('utf-8')
    manipulated_data = json.loads(raw_data)

    # Create schema object
    device_location = DeviceLocation
    device_location.device_id = manipulated_data['device_id']
    device_location.x_coordinate = manipulated_data['x_coordinate']
    device_location.y_coordinate = manipulated_data['y_coordinate']

    create_location_repository(data=device_location, db_session=db_session)
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Create location {data} is completed"
        )
    )
    db_session.close()
    return 200
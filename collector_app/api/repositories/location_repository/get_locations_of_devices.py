from ....db.db_session_middleware import db_session_middleware
from ....db.models import Location
from sqlalchemy.sql import select
from ....log_service import write_system_logging_message
from ....schema import SystemLogPydantic

def get_locations_of_device_repository(device_id: str, db_session: db_session_middleware, get_last = False):
    
    if get_last:
        """
        Get last location of device
        """
        get_all_devices_query = select(Location).where(Location.device_id==device_id).order_by(Location.create_date.desc())
        devices = db_session.execute(get_all_devices_query).scalars().first()
        write_system_logging_message(
            SystemLogPydantic(
                type="INFO", 
                message=f"Get last location of {device_id} is successfull"
            )
        )
        return devices
    
    else:
        """
        Get location history of device
        """
        get_all_devices_query = select(Location).where(Location.device_id==device_id).order_by(Location.create_date.desc())
        devices = db_session.execute(get_all_devices_query).scalars().all()
        write_system_logging_message(
            SystemLogPydantic(
                type="INFO", 
                message=f"Get location history of {device_id} is successfull"
            )
        )
        return devices

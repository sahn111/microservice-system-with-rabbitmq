from ....schema import CreateDeviceModel, SystemLogPydantic
from ....db.db_session_middleware import db_session_middleware
from ....db.models import Device
from sqlalchemy.sql import select
from ....log_service import write_system_logging_message

def get_all_devices_repository(db_session : db_session_middleware):
    get_all_devices_query = select(Device)
    devices = db_session.execute(get_all_devices_query).scalars().all()
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Get all devices is successfull"
        )
    )
    return devices

from ....schema import CreateDeviceModel, SystemLogPydantic
from ....db.db_session_middleware import db_session_middleware
from ....db.models import Device
from sqlalchemy.sql import select
from ....log_service import write_system_logging_message

def get_device_repository(device_id : str, db_session : db_session_middleware):
    get_device_query = select(Device).where(Device.device_id == device_id)
    device = db_session.execute(get_device_query).scalars().all()
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Get device {device_id} is successfull"
        )
    )
    return device
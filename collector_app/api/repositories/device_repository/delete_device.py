from ....schema import CreateDeviceModel, SystemLogPydantic
from ....db.db_session_middleware import db_session_middleware
from sqlalchemy.sql import delete
from ....db.models import Device
from ....log_service import write_system_logging_message

def delete_device_repository(device_id : str, db_session : db_session_middleware):
    delete_device_query = delete(Device).where(Device.device_id == device_id)
    db_session.execute(delete_device_query)
    db_session.commit() 
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Delete device {device_id} is successfull"
        )
    )
    return 200

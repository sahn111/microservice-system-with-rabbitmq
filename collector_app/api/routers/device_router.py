from fastapi import APIRouter, Depends
from typing import Optional
from ..services import create_device_service, get_device_service, delete_device_service
from ...db.db_session_middleware import db_session_middleware
from ...schema import CreateDeviceModel, SystemLogPydantic
from ...log_service import write_system_logging_message

router = APIRouter(
    prefix="/device",
    tags=["device"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_device_router(
    data : CreateDeviceModel,
    db_session = Depends(db_session_middleware)
):
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message="Create device router started successfully"
        )
    )
    create_device_service(data=data, db_session=db_session)
    return 200

@router.get("")
async def get_device_router(
    device_id : Optional[str] = None,
    db_session = Depends(db_session_middleware)
):
    if device_id:
        write_system_logging_message(
            SystemLogPydantic(
                type="INFO", 
                message="Get single device router started"
            )
        )
        return get_device_service(device_id=device_id, db_session=db_session)
    else:
        write_system_logging_message(
            SystemLogPydantic(
                type="INFO", 
                message="Get all devices router started"
            )
        )
        return get_device_service(db_session=db_session)

@router.delete("/{device_id}")
async def delete_device_router(
    device_id : str,
    db_session = Depends(db_session_middleware)
):
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message="Delete device router started"
        )
    )
    delete_device_service(device_id=device_id, db_session=db_session)
    return 200
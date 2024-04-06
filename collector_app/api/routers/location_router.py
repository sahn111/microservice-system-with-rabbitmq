from fastapi import APIRouter, Depends
from typing import Optional

from ..services import get_last_location_of_device_service, get_location_history_of_device_service
from ...db.db_session_middleware import db_session_middleware
from ...rabbitmq_config.rabbitmq_producer_instance import RabbitMQProducer, get_rabbitmq_producer
from ...schema import DeviceLocation, SystemLogPydantic
from ...log_service import write_system_logging_message

router = APIRouter(
    prefix="/location",
    tags=["location"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create_location_record(
    data : DeviceLocation,
    producer : RabbitMQProducer = Depends(get_rabbitmq_producer)
) -> int:
    """
    This endpoint will get too much requests
    """
    try:
        write_system_logging_message(
            SystemLogPydantic(
                type="INFO", 
                message=f"Location information for {data} send to queue"
            )
        )
        await producer.publish("hello", data.json())
        return 200
    except Exception as e:
        return 500

@router.get("/last_locations")
async def get_last_locations_of_devices(
    device_id : Optional[str] = None,
    db_session = Depends(db_session_middleware)
):
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Get last location of device router started"
        )
    )
    return get_last_location_of_device_service(device_id=device_id, db_session=db_session)
    
@router.get("/history")
async def get_location_history_of_device(
    device_id : Optional[str] = None,
    db_session = Depends(db_session_middleware)
):
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message=f"Get location history of device router started"
        )
    )
    return get_location_history_of_device_service(device_id=device_id, db_session=db_session)
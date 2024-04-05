from fastapi import APIRouter, Depends
from typing import Optional

from ..services import get_last_location_of_device_service, get_location_history_of_device_service
from ...db.db_session_middleware import db_session_middleware
from ...rabbitmq_config.rabbitmq_producer_instance import RabbitMQProducer, get_rabbitmq_producer
from ...schema import DeviceLocation

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
        print(data.json())
        await producer.publish("hello", data.json())
        return 200
    except Exception as e:
        return 500

@router.get("/last_locations")
async def get_last_locations_of_devices(
    device_id : Optional[str] = None,
    db_session = Depends(db_session_middleware)
):
    get_last_location_of_device_service(device_id=device_id, db_session=db_session)
    return 200

@router.get("/history")
async def get_location_history_of_devices(
    device_id : Optional[str] = None,
    db_session = Depends(db_session_middleware)
):
    get_location_history_of_device_service(device_id=device_id, db_session=db_session)
    return 200
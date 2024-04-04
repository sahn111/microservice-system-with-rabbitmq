from fastapi import APIRouter, Depends

from ..services import create_device_service, get_device_service, delete_device_service
from ...db.db_session_middleware import db_session_middleware
from ...schema import CreateDeviceModel

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
    create_device_service(data=data, db_session=db_session)
    return 200

@router.get("")
async def get_all_devices_router(
    db_session = Depends(db_session_middleware)
):
    get_device_service(db_session=db_session)
    return 200

@router.get("/{device_id}")
async def get_single_device_router(
    device_id : str,
    db_session = Depends(db_session_middleware)
):
    get_device_service(device_id=device_id, db_session=db_session)
    return 200

@router.delete("/{device_id}")
async def delete_device_router(
    device_id : str,
    db_session = Depends(db_session_middleware)
):
    delete_device_service(device_id=device_id, db_session=db_session)
    return 200
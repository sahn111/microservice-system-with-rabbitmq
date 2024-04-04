from typing import List
from fastapi import APIRouter, HTTPException, Depends

from ..services import *
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
    return 200

@router.get("")
async def get_all_devices_router(
    db_session = Depends(db_session_middleware)
):
    return 200

@router.get("/{device_id}")
async def get_single_device_router(
    device_id : str,
    db_session = Depends(db_session_middleware)
):
    return 200

@router.delete("/{device_id}")
async def delete_device_router(
    device_id : str,
    db_session = Depends(db_session_middleware)

):
    return 200
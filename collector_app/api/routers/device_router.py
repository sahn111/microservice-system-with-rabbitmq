from typing import List
from fastapi import APIRouter, HTTPException
import schema

from ..services import *

router = APIRouter(
    prefix="/device",
    tags=["device"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_device_router(
):
    ...

@router.get("")
async def get_all_devices_router(
):
    ...

@router.get("/{device_id}")
async def get_single_device_router(
    device_id : str
):
    ...

@router.delete("/{device_id}")
async def delete_device_router(
    device_id : str
):
    ...
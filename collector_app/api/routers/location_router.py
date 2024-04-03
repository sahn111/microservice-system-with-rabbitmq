from typing import List
from fastapi import APIRouter, HTTPException
import schema

from ..services import *

router = APIRouter(
    prefix="/location",
    tags=["location"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_device_router(
):
    ...

@router.get("/last_locations")
async def get_last_locations_of_all_devices(
):
    ...

@router.get("/history")
async def get_history_by_device(
):
    ...
from fastapi import FastAPI
from .rabbitmq_config.rabbitmq_producer_instance import rabbitmq_producer
from .api.routers import *

app = FastAPI()

app.include_router(device_router.router)
app.include_router(location_router.router)

@app.on_event("startup")
async def startup_event():
    await rabbitmq_producer.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await rabbitmq_producer.close()

@app.get("/")
async def root():
    return {"message": "Producer App is running..."}
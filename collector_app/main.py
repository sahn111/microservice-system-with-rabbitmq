from fastapi import FastAPI
from .rabbitmq_config.rabbitmq_producer_instance import rabbitmq_producer
from .api.routers import *
from .log_service import write_system_logging_message
from .schema import SystemLogPydantic

app = FastAPI()

app.include_router(device_router.router)
app.include_router(location_router.router)

@app.on_event("startup")
async def startup_event():
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message="RabbitMQ producer started"
        )
    )
    await rabbitmq_producer.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await rabbitmq_producer.close()
    write_system_logging_message(
        SystemLogPydantic(
            type="INFO", 
            message="RabbitMQ producer closed"
        )
    )

@app.get("/")
async def root():
    return {"message": "Producer App is running..."}
from fastapi import FastAPI
from .rabbitmq_client import RabbitMQClient

app = FastAPI()
rabbitmq_client = RabbitMQClient("amqp://guest:guest@localhost/")

@app.on_event("startup")
async def startup_event():
    await rabbitmq_client.start_consume("hello")

@app.on_event("shutdown")
async def shutdown_event():
    await rabbitmq_client.close()
@app.get("/")
async def root():
    return {"message": "Consumer App is running..."}
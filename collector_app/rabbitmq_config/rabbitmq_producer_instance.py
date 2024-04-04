from .rabbitmq_producer import RabbitMQProducer

rabbitmq_producer = RabbitMQProducer()

def get_rabbitmq_producer():
    return rabbitmq_producer

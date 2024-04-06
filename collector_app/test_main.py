from sqlalchemy.orm.session import sessionmaker
from fastapi.testclient import TestClient
from .main import app
from .db.models import Device
from .db.db_config import sqlalchemy_engine

client = TestClient(app)

def test_db():
    Session = sessionmaker(bind=sqlalchemy_engine)
    session = Session()
    return session

def test_create_device():
    test_data = {
        "device_name": "TestDevice",
    }

    response = client.post("/device/create", json=test_data)
    assert response.status_code == 200

    with test_db() as session:
        device = session.query(Device).filter(Device.device_name == test_data["device_name"]).first()
        # Assert that the device exists in the database
        assert device is not None

def test_get_single_device():
    response = client.get("/device")
    assert response.status_code == 200
from .api.services import create_location_service
import json

def test_create_device():
    test_data = {
        "device_id": "string",
        "x_coordinate": "string",
        "y_coordinate": "string"
    }
    test_data = json.dumps(test_data, indent=2).encode('utf-8')
    response = create_location_service(data=test_data)
    assert response == 200
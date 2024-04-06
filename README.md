# Microservice System README

This README provides an overview of the microservice system consisting of two FastAPI APIs, `collector_app`, and `consumer_app`, connected via RabbitMQ. The `collector_app` is responsible for handling device-related operations, while the `consumer_app` consumes messages from RabbitMQ and saves them to the database.

Database tables are created for mock data. It can be improved.

## Collector App

The `collector_app` contains endpoints related to device management and location tracking.

### Endpoints

#### Device Management

- **Create Device**: `POST /device/create`
  - Creates a new device entry in the database.
  - Request Body: JSON representing device information.
  - Dependencies: `db_session_middleware` for database session handling.
  
- **Get Device**: `GET /device`
  - Retrieves either all devices or a specific device by ID from the database.
  - Query Parameters: `device_id` (optional) for filtering.
  - Dependencies: `db_session_middleware` for database session handling.

- **Delete Device**: `DELETE /device/{device_id}`
  - Deletes a device entry from the database by ID.
  - Path Parameters: `device_id` for identifying the device to delete.
  - Dependencies: `db_session_middleware` for database session handling.

#### Location Tracking

- **Create Location Record**: `POST /location/`
  - Publishes location information of a device to RabbitMQ for further processing.
  - Request Body: JSON representing device location.
  - Dependencies: `get_rabbitmq_producer` for RabbitMQ producer instance.

- **Get Last Locations of Devices**: `GET /location/last_locations`
  - Retrieves the last known locations of all devices or a specific device from the database.
  - Query Parameters: `device_id` (optional) for filtering.
  - Dependencies: `db_session_middleware` for database session handling.

- **Get Location History of Device**: `GET /location/history`
  - Retrieves the location history of all devices or a specific device from the database.
  - Query Parameters: `device_id` (optional) for filtering.
  - Dependencies: `db_session_middleware` for database session handling.

## Consumer App

The `consumer_app` is responsible for consuming messages from RabbitMQ and saving them to the database.

### Purpose

- **Message Consumer**: Consumes messages from RabbitMQ and saves them to the database.

### Dependencies

- RabbitMQ: Acts as a message broker for communication between `collector_app` and `consumer_app`.
- Database: Stores device information and location data.

## Getting Started

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up RabbitMQ and ensure it's accessible to both `collector_app` and `consumer_app`.
4. Configure database connection details.
5. Start the `collector_app` and `consumer_app` services. They will automatically connect to the rabbitmq server

## Contributors

- Ali Sahin

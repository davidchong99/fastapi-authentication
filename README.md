# fastapi-authentication
This API demonstrates 2 ways to perform authentication with FastAPI:
* API key
* JWT token

## Compilation
```console
sudo apt install build-essential python3-dev libpq-dev -y
cd fastapi-authentication
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
docker compose up --build
```
To kill the server, press ctrl + c on the keyboard.

## API Usage Guide
This API has 2 functionalities or endpoints. The following show a sample usage.
1. To get metric data with API key authentication: 
```console
curl -X GET localhost:8080/metrics/get_metric/1 -H 'x-api-key: 7oDYjo3d9r58ETYYi5x4E8'
```
The response returned is as below:
```console
{"id":1,"name":"Productivity","value":100}
```
2. To get organization data with JWT token authentication:
```console
curl -X GET localhost:8080/organization/get_organization -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGF2aWQiLCJvcmdhbml6YXRpb24iOiJBQkMgQ29ycCIsInBlcm1pc3Npb25zIjpbInJlYWQiXSwiZXhwIjoxNzM5NDQxOTk2fQ.hDVW-gQQ90MOHI7ayUehgYu_rDH6YLkCKjIyWcnj3GM'
```
A valid JWT token can be generated with `jwt_auth_token` function in /tests/conftest.py.

The response returned is as below:
```console
{"org":"ABC Corp"}
```
## Architecture
All source codes are in /app directory.

main.py serves as the main entry point of this API.

There are 2 routers: 
* metric_router
* organization_router

The business logic for the endpoints are defined in the service.py

The data transfer objects are defined in dto.py.

## Tests
End-to-end tests are found in tests/e2e_tests. 

The run_tests.sh script will set up the env before running all tests with pytest.



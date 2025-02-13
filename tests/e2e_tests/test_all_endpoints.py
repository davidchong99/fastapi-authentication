import requests

BASE_URL = "http://localhost:8080"


def test_metric_endpoint(api_key):
    response = requests.get(f"{BASE_URL}/metrics/get_metric/1", headers=api_key)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Productivity"
    assert data["value"] == 100


def test_metric_endpoint_without_api_key():
    response = requests.get(f"{BASE_URL}/metrics/get_metric/1")
    assert response.status_code == 403
    data = response.json()
    assert data["detail"] == "Not authenticated"


def test_metric_endpoint_invalid_api_key(invalid_api_key):
    response = requests.get(f"{BASE_URL}/metrics/get_metric/1", headers=invalid_api_key)
    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Unauthorized"


def test_organization_endpoint(jwt_auth_token):
    response = requests.get(
        f"{BASE_URL}/organization/get_organization", headers=jwt_auth_token
    )
    assert response.status_code == 200
    data = response.json()
    assert data["org"] == "ABC Corp"


def test_organization_endpoint_no_jwt():
    response = requests.get(f"{BASE_URL}/organization/get_organization")
    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Not authenticated"


def test_organization_endpoint_no_permission(jwt_auth_token_no_permissions):
    response = requests.get(
        f"{BASE_URL}/organization/get_organization",
        headers=jwt_auth_token_no_permissions,
    )
    assert response.status_code == 403
    data = response.json()
    assert data["detail"] == "Operation not permitted"


def test_organization_endpoint_invalid_token_format(jwt_auth_token_invalid_format):
    response = requests.get(
        f"{BASE_URL}/organization/get_organization",
        headers=jwt_auth_token_invalid_format,
    )
    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Invalid token format"

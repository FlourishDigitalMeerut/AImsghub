import pytest # pyright: ignore[reportMissingImports]
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock
from main import app

@pytest.fixture(scope="session")
def client():
    return TestClient(app)


# ---------------------------
#  MOCK CURRENT USER PROVIDER
# ---------------------------
@pytest.fixture
def mock_user():
    return {
        "_id": "testuserid123",
        "email": "test@example.com",
        "name": "Test User"
    }


@pytest.fixture(autouse=True)
def override_user_dependency(mock_user):
    from services.auth import get_current_user
    app.dependency_overrides[get_current_user] = lambda: mock_user
    yield
    app.dependency_overrides.pop(get_current_user, None)


# ---------------------------
#  MOCK MONGO COLLECTION
# ---------------------------
@pytest.fixture
def mock_collection():
    collection = MagicMock()
    collection.find_one = AsyncMock(return_value=None)
    collection.insert_one = AsyncMock(return_value={"inserted_id": "mock_id"})
    collection.update_one = AsyncMock(return_value={"modified_count": 1})
    collection.find = MagicMock(return_value=[])
    return collection


@pytest.fixture(autouse=True)
def override_db(mock_collection):
    from services.database import get_users_collection, get_api_keys_collection, get_devices_collection
    app.dependency_overrides[get_users_collection] = lambda: mock_collection
    app.dependency_overrides[get_api_keys_collection] = lambda: mock_collection
    app.dependency_overrides[get_devices_collection] = lambda: mock_collection
    yield
    app.dependency_overrides.clear()

from fastapi.testclient import TestClient

from main import app

client = TestClient(app, base_url="http://test/api/v1")
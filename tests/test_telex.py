from tests import client
import json


def test_send_from_telex_success():
    response = client.post(
        "/webhook/telex?is_test=true",
        json={
            "message": '[{"id": "8ce4cf04f4rw6w8600675237350b14b4", "message": "cleanup user auth", "timestamp": "2025-02-18T10:17:54+01:00", "url": "https://github.com/8", "author": {"name": "test", "email": "test@gmail.com"}}]',
            "settings": [
                {
                    "label": "commit_types",
                    "type": "text",
                    "description": "Custom commit types and keywords",
                    "required": False,
                    "default": "{'feat': ['add', 'implement', 'new', 'introduce'], 'fix': ['fix', 'resolve', 'patch', 'address']}",
                }
            ],
        },
    )
    assert response.status_code == 200
    response_data = json.loads(response.content.decode())
    assert "refactor" in response_data

from tests import client
import json


def test_send_to_telex_success():
    response = client.post(
        "/webhook/github/{telex_channel_id}/?is_test=true",  # Replace with an existing channel ID to receive messages
        json={
            "pusher": {"name": "test"},
            "commits": [
                {
                    "id": "commit_hash",
                    "message": "commit_message",
                    "timestamp": "2025-02-18T10:17:54+01:00",
                    "url": "commit_url",
                    "author": {"name": "author_name", "email": "author_email"}
                }
            ],
        },
    )
    assert response.status_code == 200


def test_send_to_telex_failure():
    response = client.post(
        "/webhook/github/{telex_channel_id}/?is_test=true", json={"pusher": {"name": "test"}}
    )
    assert response.status_code == 422
    response_data = json.loads(response.content.decode())
    assert "commits" in response_data["detail"][0]["loc"]

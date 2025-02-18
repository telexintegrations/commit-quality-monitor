from tests import client
import json


def test_send_to_telex_success():
    response = client.post(
        "/webhook/github/{telex_channel_id}",  # Replace with an existing channel ID to receive messages
        json={
            "pusher": {"name": "test"},
            "commits": [
                {"key": "value"},
            ],
        },
    )
    assert response.status_code == 200
    response_data = json.loads(response.content.decode())
    assert response_data["data"]["status"] == "success"
    assert response_data["data"]["status_code"] == 202


def test_send_to_telex_failure():
    response = client.post(
        "/webhook/github/{telex_channel_id}", json={"pusher": {"name": "test"}}
    )
    assert response.status_code == 422
    response_data = json.loads(response.content.decode())
    assert "commits" in response_data["detail"][0]["loc"]

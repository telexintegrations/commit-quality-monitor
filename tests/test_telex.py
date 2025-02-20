from tests import client
import json


def test_send_from_telex_success():
    response = client.post(
        "/webhook/telex?is_test=true",
        json={
            "message": '[{"id": "8ce4cf04f4rw6w8600675237350b14b4", "message": "fix(auth): child\n\nFixed a race condition in the token refresh logic by implementing proper synchronization mechanisms.", "timestamp": "2025-02-18T10:17:54+01:00", "url": "https://github.com/8", "author": {"name": "test", "email": "test@gmail.com"}}]',
            "settings": [
                {
                    "label": "commit_types",
                    "type": "text",
                    "description": "Custom commit types and keywords",
                    "required": False,
                    "default": "{'feat': ['add', 'implement', 'new', 'introduce'], 'fix': ['fix', 'resolve', 'patch', 'address']}",
                },
                {
                    "label": "Example Commits",
                    "type": "text",
                    "required": True,
                    "description": "Set example commits for each custom commit type to guide new devs. These appear in suggestions when similar commits need fixing. Format: {'type1': 'example message1', 'type2': 'example message 2'}.",
                    "default": "{'feat': 'feat(auth): implement OAuth2 with role-based access\n\nImplemented OAuth2 protocol with role-based control to enhance security and scalability.', 'fix': 'fix(api): resolve data race in concurrent requests\n\nFixed a race condition by adding synchronization mechanisms to prevent concurrent data modifications.'}"
                }
            ],
        },
    )
    assert response.status_code == 200
    
    
    
    
    
def test_send_from_telex_failure():
    response = client.post(
        "/webhook/telex?is_test=true",
        json={
            "message": '[{"id": "8ce4cf04f4rw6w8600675237350b14b4", "message": "fix(auth): child\n\nFixed a race condcvghdczhjvjhzcvhjvzhjvhjvczjonization mechanisms.", "timestamp": "2025-02-18T10:17:54+01:00", "url": "https://github.com/8", "author": {"name": "test", "email": "test@gmail.com"}}]',
            "settings": [
                {
                   "label": "slack_url",
                   "type": "text",
                   "required": True,
                   "description": "Slack Webhook URL",
                   "default": "https://slack.com"
                },
                {
                    "label": "commit_types",
                    "type": "text",
                    "description": "Custom commit types and keywords",
                    "required": False,
                    "default": "",
                },
                {
                    "label": "Example Commits",
                    "type": "text",
                    "required": True,
                    "description": "Set example commits for each custom commit type to guide new devs. These appear in suggestions when similar commits need fixing. Format: {'type1': 'example message1', 'type2': 'example message 2'}.",
                    "default": "{'feat': 'feat(auth): implement OAuth2 with role-based access\n\nImplemented OAuth2 protocol with role-based control to enhance security and scalability.', 'fix': 'fix(api): resolve data race in concurrent requests\n\nFixed a race condition by adding synchronization mechanisms to prevent concurrent data modifications.'}"
                }
            ],
        },
    )
    assert response.status_code == 200
    response_data = json.loads(response.content.decode())
    for word in ("Potential gibberish words", "too brief"):
        assert word in response_data 

from tests import client
import json


def test_send_from_telex_success():
    response = client.post(
        "/webhook/telex/?is_test=true",
        json={
            "message": """
                📝 *Commit Details*
                └─ Hash: `bf238b5e`
                └─ Author: test (test@gmail.com)
                └─ URL: <https://github.com/test/test/commit/bf558b8e34dffbb20cabf1e52fe72937cac0d62c|commit url>
                └─ Time: 7:10AM. Monday, February 17, 2025.
                └─ Message:
                • ```remove unnecessary comment```

                🔍 *Analysis Results*
                🔴 Commit message type unidentifiable
                └─ Seperate the commit type from the rest of the subject using ':'.
                🔵 Commit message may be missing detailed context
                └─ Consider splitting your commit message into a concise subject and a detailed body.

                💡 Resources
                └─ Conventional Commits: <https://www.conventionalcommits.org|Conventional Commits>
                └─ Commit Best Practices: <https://dev.to/sheraz4194/good-commit-vs-bad-commit-best-practices-for-git-1plc|Best Practices>
                └─ Git Best Practices: <https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project|Git Contributing>
            """,
            "settings": [
                {
                    "label": "slack_url",
                    "type": "text",
                    "default": "https://slack.com"
                }
            ],
        },
    )
    assert response.status_code == 200
    response_data = json.loads(response.content.decode())
    for word in ("Commit message type unidentifiable", "missing detailed context"):
        assert word in response_data
    
    
    
    
    
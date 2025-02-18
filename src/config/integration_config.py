from datetime import datetime
from .config import settings


def generate_json_config():
    return {
        "data": {
            "date": {
                "created_at": f"{datetime.now().isoformat()}",
                "updated_at": f"{datetime.now().isoformat()}"
            },
            "descriptions": {
            "app_description": "Checks GitHub commit messages for quality standards and provides detailed analysis and improvement suggestions on problematic commits.",
            "app_logo": settings.app_logo_url,
            "app_name": "GitHub Commit Quality Monitor",
            "app_url": settings.app_url,
            "background_color": f"#{settings.background_color_hexcode}"
            },
            "integration_category": "Development & Code Management",
            "integration_type": "output",
            "is_active": False,
            "key_features": [
                "Comprehensive quality checks on structure, content, and context",
                "Configurable type indicators for custom commit conventions",
                "Real-time feedback with specific improvement suggestions",
            ],
            "settings": [
                {
                    "label": "commit_types",
                    "type": "text",
                    "description": "Custom commit types and keywords",
                    "required": False,
                    "default": "{'feat': ['add', 'implement', 'new', 'introduce'], 'fix': ['fix', 'resolve', 'patch', 'address']}"
                },
                {
                    "label": "example_commits",
                    "type": "text",
                    "description": "Custom Example Commits",
                    "required": False,
                    "default": "{'feat': 'feat(auth): implement 0Auth2 with role-based access', 'fix': 'fix(api): resolve data race in concurrent requests'}"
                },
                {
                    "label": "training_data",
                    "type": "text",
                    "description": "Custom Training Data",
                    "required": False,
                    "default": "{'feat': ['feat(ui): add dark mode toggle with system preference detection','feat(auth): implement JWT authentication flow','feat(api): implement rate limiting middleware','feat(forms): add client-side form validation','feat(search): implement elasticsearch integration','feat(cache): add Redis caching layer for API responses','feat(auth): implement social login providers','feat(security): add two-factor authentication support']}"
                }
            ],
            "target_url": settings.target_url
        }
    }
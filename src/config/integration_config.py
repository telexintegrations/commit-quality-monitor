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
                "Smart commit message analysis with ML-powered suggestions",
                "Customizable commit rules that fit any team's style",
                "Instant notifications when commits need attention",
                "Easy setup with pre-configured commit patterns"
            ],
            "settings": [
                {
                    "label": "commit_types",
                    "type": "text",
                    "description": "Provide custom commit types mapped to keywords that indicate type of change. Format: {'type': ['keyword1', 'keyword2']}. Example: {'docs': ['document', 'readme']} means commits with 'document' or 'readme' suggest documentation changes.",
                    "required": False,
                    "default": "{'feat': ['add', 'implement', 'new', 'introduce'], 'fix': ['fix', 'resolve', 'patch', 'address']}"
                },
                {
                    "label": "example_commits",
                    "type": "text",
                    "description": "Set example commits for each custom commit type to guide new devs. These appear in suggestions when similar commits need fixing. Format: {'type1': 'example message1', 'type2': 'example message 2'}.",
                    "required": False,
                    "default": "{'feat': 'feat(auth): implement 0Auth2 with role-based access', 'fix': 'fix(api): resolve data race in concurrent requests'}"
                },
                {
                    "label": "training_data",
                    "type": "text",
                    "description": "Add custom data to train the analyzer with commits that match preferred style. More examples = better suggestions. Format: {'type1': ['example1', 'example2'], 'type2': ['example3', 'example4']}. The analyzer learns from these to better match preferred conventions.",
                    "required": False,
                    "default": "{'feat': ['feat(ui): add dark mode toggle with system preference detection','feat(auth): implement JWT authentication flow','feat(api): implement rate limiting middleware','feat(forms): add client-side form validation','feat(search): implement elasticsearch integration','feat(cache): add Redis caching layer for API responses','feat(auth): implement social login providers','feat(security): add two-factor authentication support']}"
                }
            ],
            "target_url": settings.target_url
        }
    }
from datetime import datetime
from .config import settings


def generate_json_config():
    return {
        "data": {
            "date": {
                "created_at": f"{datetime.now().strftime('%-I:%M%p. %A, %B %-d, %Y.')}",
                "updated_at": f"{datetime.now().strftime('%-I:%M%p. %A, %B %-d, %Y.')}"
            },
            "descriptions": {
                "app_name": "GitHub Commit Quality Monitor",
                "app_description": "Checks GitHub commit messages for quality standards and provides detailed analysis and improvement suggestions on problematic commits.",
                "app_logo": settings.app_logo_url,
                "app_url": settings.app_url,
                "background_color": f"#{settings.background_color_hexcode}"
            },
            "is_active": True,
            "integration_category": "Development & Code Management",
            "integration_type": "output",
            "key_features": [
                "Smart commit message analysis with ML-powered suggestions",
                "Instant notifications when commits need attention",
                "Easy setup with pre-configured commit patterns"
            ],
            "website": settings.app_url,
            "author": "iamprecieee",
            "settings": [
                {
                   "label": "slack_url",
                   "type": "text",
                   "required": True,
                   "description": "Slack Webhook URL",
                   "default": "https://slack.com"
                }
            ],
            "target_url": settings.target_url
        }
    }

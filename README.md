# Git Commit Quality Monitor

A smart Telex integration that helps teams maintain high-quality git commit messages using ML-powered analysis and real-time feedback.

## Overview

Git Commit Quality Monitor analyzes commit messages in real-time, providing instant feedback on commit quality and suggestions for improvement. It uses machine learning to understand commit patterns and provides customized suggestions based on conventional commit standards and the development team's preferences.

### Key Features

- ⚡️ Real-time feedback through Slack
- 🎯 Customizable commit rules/conventions
- 🔄 GitHub webhook integration
- 🎨 Telex integration support
- 🤖 Smart ML-powered commit message analysis and suggestions

## Quick Start Guide

### Prerequisites

- Python 3.8+
- FastAPI
- scikit-learn
- Git (for development)
- Telex account
- GitHub repository access
- Slack workspace (for notifications)

### Basic Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd commit-quality-monitor
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

### Integration Setup

1. Configure repository webhooks with specific settings:
    - Go to your repository settings
    - Add webhook: `<your-app-url>/api/v1/webhook/github/{telex_channel_id}`
    - Set content type to `application/json`
    - Select "Just the push event"

2. Configure Slack notifications:
   - Create a Slack app
   - Add Incoming Webhooks
   - Add the generated webhook URL to your environment variables

## Detailed Configuration

| Variable | Description | Example |
|----------|-------------|---------|
| ALLOWED_ORIGINS | Comma-separated list of allowed origins | https://github.com,http://localhost:8000 |
| ALLOWED_HOSTS | Comma-separated list of allowed hosts | github.com,localhost |
| HOST | Server host | 0.0.0.0 |
| PORT | Server port | 8000 |
| TELEX_WEBHOOK_URL | Telex webhook URL | https://ping.telex.im/v1/webhooks |
| SLACK_URL | Slack webhook URL for notifications | https://hooks.slack.com/... |
| APP_LOGO_URL | URL for app logo | https://example.com/logo.png |
| APP_URL | Application URL | https://your-app.com |
| TARGET_URL | Telex target URL | https://your-app.com/webhook/telex |

## System Architecture

### Project Structure

```
project_root/
├── src/
│   ├── core/                      # Core Analysis Engine
│   │   ├── analyzer.py            # ML-based commit analysis logic
│   │   └── models.py              # Data models and structure
│   │
│   ├── config/                    # Configuration Management
│   │   ├── data.py                # Training data, patterns, and examples
│   │   ├── config.py              # Environment settings management
│   │   ├── integration_config.py  # Telex integration configuration
│   │   └── middleware.py          # CORS and trusted host middleware
│   │
│   ├── routers/                   # API Routing Layer
│   │   ├── github.py              # GitHub webhook endpoint handling
│   │   ├── telex.py               # Telex webhook and integration
│   │   └── router.py              # Main router configuration
│   │
│   └── utils/                     # Utility Functions
│       └── telex_utils.py         # Telex communication helpers
│
├── tests/                         # Test Suite
│   ├── __init__.py                # Test configuration
│   ├── test_github.py             # GitHub integration tests
│   └── test_telex.py              # Telex integration tests
│
├── .env.example                   # Environment variable template
├── main.py                        # Application entry point
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
```

### Core Analysis Engine

The system implements a multi-step process to evaluate the quality of commit messages:

#### Direct Pattern Matching
   - Matches against predefined commit types
   - Provides immediate classification
   - Optimized for standard conventions

```python
commit_types = {
    "feat": ["add", "implement", "new", "introduce"],
    "fix": ["fix", "resolve", "patch", "address"],
    "docs": ["document", "update docs", "readme"],
    "refactor": ["refactor", "restructure", "simplify"]
}
```

#### Machine Learning Classification
   - Uses TF-IDF vectorization to transform commit messages into numerical vectors
   - Maintains a training dataset of exemplar commits
   - Employs cosine similarity analysis to compute similarity scores against known patterns
   - Suggests types based on highest similarity matches

```python
def _prepare_ml_classifier(self):
    x_train = []  # Commit messages
    y_train = []  # Corresponding types
    
    for commit_type, messages in self.commit_training_data.items():
        x_train.extend(messages)
        y_train.extend([commit_type] * len(messages))
        
    self.vectorizer.fit(x_train)
    self.x_train_vectorized = self.vectorizer.transform(x_train)
```

#### Semantic Analysis
   - Recognizes complex patterns
   - Understands contextual relationships
   - Handles non-standard commits

```python
semantic_patterns = {
    "feat": [
        ("create", "new"),
        ("add", "feature"),
        ("implement", "support")
    ],
    "fix": [
        ("resolve", "issue"),
        ("patch", "vulnerability"),
        ("correct", "behavior")
    ]
}
```

#### Content Quality
- It verifies that the commit message contains enough words. Messages with fewer than 5 words are flagged with a high-severity warning, while those with 5–9 words are flagged with a medium-severity warning. 
- Scans the commit message for words that might be gibberish. 

#### Context Evaluation
- Ensures that the commit message provides adequate context. It looks for a clear separation between the subject line and the detailed body (detected via a double newline \n\n). If this separation is missing, the method suggests splitting the message to improve clarity.

## API Documentation

### GitHub Webhook Endpoint
```http
POST /api/v1/webhook/github/{telex_channel_id}
Content-Type: application/json

{
    "pusher": {"name": "username"},
    "commits": [
        {
            "id": "commit_hash",
            "message": "commit_message",
            "timestamp": "iso_timestamp"
        }
    ]
}
```
Receives GitHub push events and forwards to Telex.

### Telex Integration Endpoint
```http
POST /api/v1/webhook/telex
Content-Type: application/json

{
    "message": "serialized_commit_data",
    "settings": [
        {
            "label": "commit_types",
            "type": "text",
            "default": "{...}"
        }
    ]
}
```
Receives commit messages from Telex and sends analysis results to slack.

### Integration Config
```
GET /integration.json
```
Returns integration configuration for Telex.

### Customizing Commit Analysis

You can customize the analyzer through Telex integration settings:

#### Commit Types
```json
{
    "feat": ["add", "implement", "new"],
    "fix": ["fix", "resolve", "patch"]
}
```

#### Example Commits
```json
{
    "feat": "feat(auth): implement OAuth2 with role-based access\n\nImplemented OAuth2 protocol with role-based control to enhance security and scalability.",
    "fix": "fix(api): resolve data race in concurrent requests\n\nFixed a race condition by adding synchronization mechanisms to prevent concurrent data modifications."
}
```

#### Training Data
```json
{
    "feat": [
        "feat(ui): add dark mode toggle",
        "feat(api): implement rate limiting"
    ]
}
```

## Development Guide

### Running the Application
```bash
uvicorn main:app --reload
```

### Testing
```bash
pytest tests/
```

### Contributing

To contribute to the project:
1. Fork the repository
2. Create a feature branch
3. Commit changes following our guidelines
4. Push to your branch
5. Submit a Pull Request



---

📦 GitHub Push → 🔄 Telex → 🧠 Analysis/Suggestions Pipeline (🔍 → 🤖 → 🎯)  → 📱 Slack Alert
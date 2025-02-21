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

- Python 3.12
- FastAPI
- scikit-learn
- Git (for development)
- Telex account
- GitHub repository access
- Slack workspace (for notifications)

## Detailed Configuration

| Variable | Description | Example |
|----------|-------------|---------|
| ALLOWED_ORIGINS | Comma-separated list of allowed origins | https://github.com,http://localhost:8000 |
| ALLOWED_HOSTS | Comma-separated list of allowed hosts | github.com,localhost |
| HOST | Server host | 0.0.0.0 |
| PORT | Server port | 8000 |
| TELEX_WEBHOOK_URL | Telex webhook URL | https://ping.telex.im/v1/webhooks |
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
        "feat(auth): implement JWT authentication flow\n\nImplemented JWT-based authentication with token expiration handling to secure user sessions.",
        "feat(ui): add dark mode toggle with system preference detection\n\nAdded dark mode toggle that automatically adjusts based on system settings for improved user experience.",
    ],
}
```

## Development Guide

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

### Running the Application
```bash
uvicorn main:app --reload
```

### Telex Channel Setup

#### Step 1: Create Telex Channel
1. Log into your Telex account
2. Click on the ⊕ sign to add new channel
3. Fill in channel details:
   - Name: "Commit Quality Monitor"
4. Copy the channel ID - you'll need this for GitHub webhook setup

### GitHub Webhook Setup

#### Step 1: Access Repository Settings
1. Go to your GitHub repository
2. Click on "Settings" (requires admin access)
   - Located in the top menu bar
   - Look for the ⚙️ gear icon

#### Step 2: Navigate to Webhooks
1. In the left sidebar, click on "Webhooks"
2. Click the "Add webhook" button (top right)

#### Step 3: Configure Webhook
1. Fill in the following fields:
   - Payload URL: `https://your-domain/api/v1/webhook/github/{telex_channel_id}`
   - Replace `your-domain` with your actual domain
   - Replace `{telex_channel_id}` with your Telex channel ID
2. Set Content Type:
   - Select "application/json" from the dropdown menu
3. Select Events:
   - Choose "Just the push event"
   - This ensures you only receive relevant commit notifications
4. Check "Active":
   - Ensure the webhook is enabled
5. Click "Add webhook" to save

#### Step 4: Verify Configuration
1. Check the webhook in your repository settings
2. Look for a green checkmark indicating successful configuration
3. If you see a red X, check the "Recent Deliveries" tab for error details

### Slack Integration Setup

#### Step 1: Create Slack App
1. Visit [Slack API Portal](https://api.slack.com/apps)
2. Click "Create New App"
3. Choose "From scratch"
4. Fill in app details:
   - App Name: "Commit Quality Guardian"
   - Choose your workspace
   - Click "Create App"

#### Step 2: Configure Incoming Webhooks
1. In your app's settings page:
   - Click "Incoming Webhooks" in the left sidebar
   - Toggle "Activate Incoming Webhooks" to `On`
2. Add New Webhook:
   - Click "Add New Webhook to Workspace"
   - Choose the channel where notifications should appear
   - Click "Allow"
3. Copy Webhook URL:
   - Find the new webhook URL in the list
   - Copy it - you'll need this for configuration in Telex
   - Format: `https://hooks.slack.com/services/XXX/YYY/ZZZ`

### Telex Integration Setup

#### Step 1: Add Integration to Channel
1. In the left menu on your telex dashboard:
   - Click "Apps"
   - Click "Add New"
   - Enter the Integration JSON url: `https://your-domain/integration.json`
2. Configure Integration:
   - Click on "Manage App" beside the added integration
   - Click on "Settings"
   - Add the slack webhook in the `slack_url` field
   - Clear defaults in `commit_types`, `example_commits`, and `training_data` fields; replace with custom values if necessary.

#### Step 3: Save and Activate
1. Click "Save Settings"
2. Enable the integration on the Apps dashboard

### Testing Your Integration

#### Step 1: Make a Test Commit
1. Clone your repository:
   ```bash
   git clone https://github.com/your-org/your-repo.git
   cd your-repo
   ```
2. Make a test commit:
   ```bash
   # Make a change
   echo "test" > test.txt
   
   # Add and commit
   git add test.txt
   git commit -m "add test file"
   
   # Push changes
   git push origin main
   ```

#### Step 2: Verify Notifications
1. Check GitHub:
   - Go to repository settings
   - Click Webhooks
   - Look for successful delivery (green checkmark)
2. Check Slack:
   - Go to your configured Slack channel
   - You should see a quality analysis message
3. Check Telex:
   - Open your Telex channel
   - Verify the message was processed

### Troubleshooting

#### Common Issues and Solutions
1. Webhook Not Triggering:
   - Verify webhook URL is correct
   - Check repository permissions
   - Ensure webhook is active
2. Slack Messages Not Appearing:
   - Verify Slack webhook URL
   - Check app permissions in Slack
   - Ensure channel exists and is accessible
   - Check application logs for errors
3. Telex Integration Issues:
   - Verify Telex channel ID
   - Check integration status in Telex
   - Ensure webhook URLs match
   - Verify settings configuration

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

---

## Test Screenshots
![Message received on Telex channel from Github](https://raw.githubusercontent.com/telexintegrations/commit-quality-monitor/staging/screenshots/telex_1.png)
![Message received on Slack channel from Telex](https://raw.githubusercontent.com/telexintegrations/commit-quality-monitor/staging/screenshots/telex_2.png)
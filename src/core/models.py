from pydantic import BaseModel
from dataclasses import dataclass


class GitHubPayload(BaseModel):
    """Represents the webhook payload from GitHub"""
    pusher: dict
    commits: list
    
    
class Commit(BaseModel):
    """Represents a commit object from the GitHub payload"""
    id: str
    author: str
    message: str
    url: str
    timestamp: str
    
    
class TelexWebhookPayload(BaseModel):
    """Represents the payload to be sent to the Telex webhook"""
    event_name: str
    message: str
    status: str
    username: str
    
    
@dataclass
class CommitIssue:
    """Represents an issue found in a commit message"""
    severity: str
    message: str
    suggestion: str
    
    
class TelexTargetPayload(BaseModel):
    """Represents the payload from the Telex-set target_url"""
    message: str
    settings: list
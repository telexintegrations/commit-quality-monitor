from ...config.data import (
    commit_types,
    example_commits,
    commit_training_data
)
from ..models import CommitIssue
from .format_analyzer import FormatAnalyzer
from .quality_analyzer import QualityAnalyzer
from datetime import datetime


class CommitAnalyzer:
    """
    Analyzes Git commit messages using a combination of pattern matching, 
    machine learning, and semantic analysis to ensure commit quality and 
    provide improvement suggestions.
    """
    def __init__(self) -> None:
        """Initializes the analyzer with commit types, examples, and training data."""
        self.commit_types = commit_types  
        self.example_commits = example_commits.copy()
        self.commit_training_data = commit_training_data.copy()

    def _check_content_format(self, message: str) -> list[CommitIssue]:
        format_analyzer = FormatAnalyzer(message, self.commit_types, self.example_commits)
        return format_analyzer.check_all()
        
    def _check_content_quality(self, message: str) -> list[CommitIssue]:
        quality_analyzer = QualityAnalyzer(message)
        return quality_analyzer.check_all()
    
    def analyze_commit(self, message: str) -> list[CommitIssue]:
        """Analyzes a commit message and returns any quality issues found."""
        issues = []
        issues.extend([*self._check_content_format(message)])
        issues.extend([*self._check_content_quality(message)])
        return [issue for issue in issues if issue]

    def format_analysis(self, commit: dict, issues: list[CommitIssue]) -> str:
        """Formats analysis results into a human-readable message for Slack."""
        icons = {"high": "🔴", "medium": "🟡", "low": "🔵"}
        
        timestamp = datetime.fromisoformat(commit["timestamp"].replace("Z", "+00:00"))
        formatted_time = timestamp.strftime("%-I:%M%p. %A, %B %-d, %Y.")
        
        author = commit["author"]
        author_info = f"{author['name']} ({author.get('email')})"

        commit_details = (
            "📝 *Commit Details*\n"
            f"└─ Hash: `{commit['id'][:8]}`\n"
            f"└─ Author: {author_info}\n"
            f"└─ URL: <{commit['url']}|commit url>\n"
            f"└─ Time: {formatted_time}\n"
            f"└─ Message:\n"
            f"• ```{commit['message']}```\n"
        )

        if issues:
            issues_text = "\n".join(
                f"{icons[issue.severity]} {issue.message}\n"
                f"   └─ {issue.suggestion.replace(chr(10), chr(10) + '     ')}"
                for issue in sorted(issues, key=lambda x: x.severity)
            )
            analysis_section = "\n🔍 *Analysis Results*\n" f"{issues_text}\n"

        suggestions = (
            "\n💡 Resources\n"
            "└─ Conventional Commits: <https://www.conventionalcommits.org|Conventional Commits>\n"
            "└─ Commit Best Practices: <https://dev.to/sheraz4194/good-commit-vs-bad-commit-best-practices-for-git-1plc|Best Practices>\n"
            "└─ Git Best Practices: <https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project|Git Contributing>"
        )

        return f"{commit_details}{analysis_section}{suggestions}"
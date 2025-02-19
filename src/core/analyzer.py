from sklearn.feature_extraction.text import TfidfVectorizer
from ..config.data import (
    commit_types,
    example_commits,
    commit_training_data,
    semantic_patterns,
)
from fastapi import HTTPException, status
from sklearn.metrics.pairwise import cosine_similarity
from .models import CommitIssue
from datetime import datetime
import ast


class CommitAnalyzer:
    """
    Analyzes Git commit messages using a combination of pattern matching, 
    machine learning, and semantic analysis to ensure commit quality and 
    provide improvement suggestions.
    """
    def __init__(self, settings: list):
        """Initializes the analyzer with custom settings and prepares the ML classifier."""
        self.settings = settings
        self.vectorizer = TfidfVectorizer()

        self.commit_types = commit_types.copy()
        self.example_commits = example_commits.copy()
        self.commit_training_data = commit_training_data.copy()
        self.semantic_patterns = semantic_patterns.copy()

        try:
            self._apply_data_settings()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid settings data: {str(e)}",
            )

        self._prepare_ml_classifier()

    def _apply_data_settings(self):
        """
        Updates analyzer configuration with custom settings provided through Telex.
        Custom settings can override default commit types, examples, and training data.
        """
        for setting in self.settings:
            if setting["label"] == "commit_types":
                self.commit_types.update(ast.literal_eval(setting["default"]))
            elif setting["label"] == "example_commits":
                self.example_commits.update(ast.literal_eval(setting["default"]))
            elif setting["label"] == "training_data":
                self.commit_training_data.update(ast.literal_eval(setting["default"]))

    def _prepare_ml_classifier(self):
        """
        Prepares the machine learning classifier for commit type prediction.
        Transforms the training dataset into TF-IDF vectors for similarity-based
        classification of commit messages.
        """
        x_train = []
        y_train = []  

        for commit_type, messages in self.commit_training_data.items():
            x_train.extend(messages)
            y_train.extend([commit_type] * len(messages))

        self.vectorizer.fit(x_train)
        self.x_train_vectorized = self.vectorizer.transform(x_train)
        self.y_train = y_train

    def _check_format(self, message: str) -> list[CommitIssue]:
        """Validates commit message format against conventional commit standards."""
        first_word = message.split("(")[0] if "(" in message else message.split(":")[0]

        if first_word.lower() not in self.commit_types:
            likely_type = self._suggest_commit_type(message)
            return [
                CommitIssue(
                    severity="high",
                    message="Invalid commit type",
                    suggestion=f"Use '{likely_type}' for this kind of change\nExample: `{self.example_commits[likely_type]}`",
                )
            ]
        return []

    def _suggest_commit_type(self, message: str) -> str:
        """Suggests the most appropriate commit type using a three-stage analysis pipeline."""
        message = message.lower()

        type_scores = {
            commit_type: sum(word in message for word in indicators)
            for commit_type, indicators in self.commit_types.items()
        }

        if any(score > 0 for score in type_scores.values()):
            return max(type_scores.items(), key=lambda x: x[1])[0]

        message_vectorized = self.vectorizer.transform([message])
        similarities = cosine_similarity(message_vectorized, self.x_train_vectorized)[0]

        if max(similarities) > 0.3:  # If we have a decent similarity match
            most_similar_idx = similarities.argmax()
            return self.y_train[most_similar_idx]

        semantic_patterns = self.semantic_patterns
        semantic_scores = {
            commit_type: sum(
                1 for pattern in patterns if any(word in message for word in pattern)
            )
            for commit_type, patterns in semantic_patterns.items()
        }

        if any(score > 0 for score in semantic_scores.values()):
            return max(semantic_scores.items(), key=lambda x: x[1])[0]

        return "chore"

    def analyze_commit(self, message: str) -> list[CommitIssue]:
        """Analyzes a commit message and returns any quality issues found."""
        issues = []
        issues.extend([*self._check_format(message)])
        return [issue for issue in issues if issue]

    def format_analysis(self, commit: dict, issues: list[CommitIssue]) -> str:
        """Formats analysis results into a human-readable message for Slack."""
        icons = {"high": "🔴", "medium": "🟡"}
        
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
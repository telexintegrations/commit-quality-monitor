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
    def __init__(self, settings: list):
        self.settings = settings
        self.vectorizer = TfidfVectorizer()

        # Core commit types and indicators, example commits, and commit training data
        self.commit_types = commit_types.copy()
        self.example_commits = example_commits.copy()
        self.commit_training_data = commit_training_data.copy()
        self.semantic_patterns = semantic_patterns.copy()

        # Apply data settings from payload
        try:
            self._apply_data_settings()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid settings data: {str(e)}",
            )

        # Initialize ML Components
        self._prepare_ml_classifier()

    def _apply_data_settings(self):
        """Applies any provided custom settings"""
        for setting in self.settings:
            if setting["label"] == "commit_types":
                self.commit_types.update(ast.literal_eval(setting["default"]))
            elif setting["label"] == "example_commits":
                self.example_commits.update(ast.literal_eval(setting["default"]))
            elif setting["label"] == "training_data":
                self.commit_training_data.update(ast.literal_eval(setting["default"]))

    def _prepare_ml_classifier(self):
        """
        Prepare the ML classiifier with training data by converting commit messages into numerical vectors
        that can be used to find similar messages.
        """
        x_train = []  # Will hold all example commit messages
        y_train = []  # Will hold the corresponding commit type for each message

        for commit_type, messages in self.commit_training_data.items():
            x_train.extend(messages)

            # For each message, add its commit type to y_train
            # e.g., if there are 5 'feat' messages, 'feat' is added 5 times to y_train
            y_train.extend([commit_type] * len(messages))

        # Transform example messages into numerical vectors using TF-IDF
        # to measure importance of each word
        self.vectorizer.fit(x_train)

        # Transform messages into numerical vector based on their words
        self.x_train_vectorized = self.vectorizer.transform(x_train)
        self.y_train = y_train

    def _check_format(self, message: str) -> list[CommitIssue]:
        """Verify commit message format"""
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
        """Suggest the most appropriate commit type using multiple approaches"""
        message = message.lower()

        # Score commit types based on how many of their indicator words appear in message
        type_scores = {
            commit_type: sum(word in message for word in indicators)
            for commit_type, indicators in self.commit_types.items()
        }

        if any(score > 0 for score in type_scores.values()):
            return max(type_scores.items(), key=lambda x: x[1])[0]

        # If no direct matches exist, try ML-based similarity
        message_vectorized = self.vectorizer.transform([message])
        similarities = cosine_similarity(message_vectorized, self.x_train_vectorized)[0]

        if max(similarities) > 0.3:  # If we have a decent similarity match
            most_similar_idx = similarities.argmax()
            return self.y_train[most_similar_idx]

        # Fallback to semantic analysis if all the above fail.  Here, check for all commit_types if any word
        # in the message matches a word in the pattern for each pattern and score accordingly.
        # Then return the item with the highest score.
        semantic_patterns = self.semantic_patterns
        semantic_scores = {
            commit_type: sum(
                1 for pattern in patterns if any(word in message for word in pattern)
            )
            for commit_type, patterns in semantic_patterns.items()
        }

        if any(score > 0 for score in semantic_scores.values()):
            return max(semantic_scores.items(), key=lambda x: x[1])[0]

        # Default to chore if nothing matches
        return "chore"

    def analyze_commit(self, message: str) -> list[CommitIssue]:
        """Main analysis method returning a list of issues"""
        issues = []

        # Core checks
        issues.extend([*self._check_format(message)])

        return [issue for issue in issues if issue]

    def format_analysis(self, commit: dict, issues: list[CommitIssue]) -> str:
        """Format analysis results for display"""
        icons = {"high": "🔴", "medium": "🟡"}

        # Format timestamp with am/pm and day name
        timestamp = datetime.fromisoformat(commit["timestamp"].replace("Z", "+00:00"))
        formatted_time = timestamp.strftime(
            "%-I:%M%p. %A, %B %-d, %Y."
        )  # %-I removes leading zero

        # Format author info
        author = commit["author"]
        author_info = f"{author['name']} ({author.get('email')})"

        # Format commit details section
        commit_details = (
            "📝 *Commit Details*\n"
            f"└─ Hash: `{commit['id'][:8]}`\n"
            f"└─ Author: {author_info}\n"
            f"└─ URL: {commit['url']}\n"
            f"└─ Time: {formatted_time}\n"
            f"└─ Message:\n"
            f"• ```{commit['message']}```\n"
        )

        # Format issues
        if issues:
            issues_text = "\n".join(
                f"{icons[issue.severity]} {issue.message}\n"
                f"   └─ {issue.suggestion.replace(chr(10), chr(10) + '     ')}"
                for issue in sorted(issues, key=lambda x: x.severity)
            )
            analysis_section = "\n🔍 *Analysis Results*\n" f"{issues_text}\n"

        # Format suggestions section
        suggestions = (
            "\n💡 Resources\n"
            "└─ Conventional Commits: https://www.conventionalcommits.org\n"
            "└─ Commit Best Practices: https://dev.to/sheraz4194/good-commit-vs-bad-commit-best-practices-for-git-1plc\n"
            "└─ Git Best Practices: https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project"
        )

        return f"{commit_details}{analysis_section}{suggestions}"

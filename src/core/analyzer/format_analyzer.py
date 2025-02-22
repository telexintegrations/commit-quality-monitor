from sklearn.feature_extraction.text import TfidfVectorizer
import string
from ..models import CommitIssue
from ...config.data import semantic_patterns
from sklearn.metrics.pairwise import cosine_similarity


class FormatAnalyzer:
    """
    Validates commit message format against conventional commit standards.
    Checks for capitalization, puctuation, length.
    Provides improvement suggestions
    """
    def __init__(self, message: str, commit_types: dict[str, str], example_commits: dict[str, str]) -> None:
        self.message = message
        self.message_parts = self.message.split("\n\n", maxsplit=1) if "\n\n" in self.message else self.message.split("\n", maxsplit=1)
        self.subject = self.message_parts[0]
        self.body = self.message_parts[1] if len(self.message_parts) > 1 else None
        self.commit_type = (
            self.subject.split("(")[0] if "(" in self.subject
            else self.subject.split(":")[0] if ":" in self.subject
            else None
        )
        self.valid_commit_types = commit_types.copy()
        self.example_commits = example_commits.copy()
        self.semantic_patterns = semantic_patterns.copy()
        self.issues = []
        
        self.vectorizer = TfidfVectorizer()
        
    def _check_subject(self) -> None:
        first_word = self.subject.split(":")[1].strip() if ":" in self.subject else None
        if first_word and any([first_word[0] != first_word[0].lower(), not first_word[0].isalpha]):
            self.issues.append(
                CommitIssue(
                    severity="high",
                    message="Subject not in lowercase",
                    suggestion="Subject must start with a lowercase letter, unless it's a proper noun or acronym."
                )
            )
            
        if self.subject.endswith(tuple(string.punctuation)):
            self.issues.append(
                CommitIssue(
                    severity="high",
                    message="Subject ends with a punctuation",
                    suggestion="Remove the punctuation at the end of the subject line."
                )
            )
            
        if len(self.subject) > 50:
            self.issues.append(
                CommitIssue(
                    severity="high",
                    message="Subject exceeds 50 characters",
                    suggestion="Subject too long, keep it under 50 characters."
                )
            )
            
    def _check_body(self) -> None:
        if not self.body:
            self.issues.append(
                CommitIssue(
                    severity="low",
                    message="Commit message may be missing detailed context",
                    suggestion="Consider splitting your commit message into a concise subject and a detailed body."
                )
            )
            return
            
        if not "\n\n" in self.message:
            self.issues.append(
                CommitIssue(
                    severity="medium",
                    message="Body missing a blank line after subject",
                    suggestion="Add a blank line between the subject and body."
                )
            )
            
        for line in self.body.split("\n"):
            if len(line) > 72:
                self.issues.append(
                    CommitIssue(
                        severity="high",
                        message="Body lines exceed 72 characters",
                        suggestion="Body lines too long, wrap text at 72 characters per line."
                    )
                )
                
    def _check_commit_type(self) -> None:
        if not self.commit_type:
            self.issues.append(
                CommitIssue(
                    severity="high",
                    message="Commit message type unidentifiable",
                    suggestion="Seperate the commit type from the rest of the subject using ':'."
                )
            )
            return
        
        if self.commit_type != self.commit_type.lower():
            self.issues.append(
                CommitIssue(
                    severity="high",
                    message="Invalid commit type case",
                    suggestion="Commit type must be lowercase (e.g., fix, feat, docs)."
                )
            )
            
        if self.commit_type.lower() not in self.valid_commit_types:
            likely_type = self._suggest_commit_type()
            self.issues.append(
                CommitIssue(
                    severity="high",
                    message="Invalid commit type",
                    suggestion=f"Use '{likely_type}' for this kind of change\n└─ Example:\n• ```{self.example_commits[likely_type]}```",
                )
            )
            
    def _suggest_commit_type(self) -> str:
        """Suggests the most appropriate commit type using a three-stage analysis pipeline."""
        message = self.message.lower()

        type_scores = {
            commit_type: sum(word in message for word in indicators)
            for commit_type, indicators in self.valid_commit_types.items()
        }

        if any(score > 0 for score in type_scores.values()):
            return max(type_scores.items(), key=lambda x: x[1])[0]

        self._prepare_ml_classifier()
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

        return "chore" # Fallback value
    
    def _prepare_ml_classifier(self) -> None:
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
            
    def check_all(self) -> list[CommitIssue]:
        self._check_subject()
        self._check_body()
        self._check_commit_type()
        return self.issues
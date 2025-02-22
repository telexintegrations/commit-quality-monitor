import string
from ..models import CommitIssue
from ...config.data import LETTER_FREQUENCY, VALID_PAIRS


class QualityAnalyzer:
    """
    Assesses the quality of the commit message content.
    Checks the commit message for potential gibberish words.
    """
    def __init__(self, message: str):
        self.words = message.split()
        self.issues = []
        
    def _run_gibberish_check(self) -> None:
        gibberish_words = [
            word.strip(string.punctuation) 
            for word in self.words 
            if self._check_gibberish(word) and word.strip(string.punctuation)
        ]
        if gibberish_words:
            self.issues.append(
                CommitIssue(
                    severity="high",
                    message="Potential gibberish words detected in commit message",
                    suggestion=f"Review and correct the following words: {', '.join(gibberish_words)}"
                )
            )
        
    def _check_gibberish(self, word: str) -> bool:
        """
        Determines if a word is likely to be gibberish using multiple linguistic patterns.
        
        The function employs four distinct checks to identify gibberish:
        1. Vowel ratio: Words must maintain a minimum vowel-to-length ratio of 0.2
        2. Consonant sequences: Flags sequences of more than 4 consecutive consonants
        3. Letter frequency: For words >= 4 chars, compares letter frequencies against English language norms
        4. Consonant pairs: Identifies invalid consonant combinations that rarely occur in English
        
        A word is considered gibberish if it fails two or more of these checks.
        """
        VOWELS = set('aeiouyAEIOUY')
            
        word = word.lower().strip(string.punctuation)
        if not word or len(word) < 2 or not word.isalpha():
            return False
        
        failed_checks = 0

        vowel_count = sum(1 for c in word if c in VOWELS)
        if vowel_count / len(word) < 0.2:
            failed_checks += 1
            
        consonant_sequence = 0
        for char in word:
            if char not in VOWELS:
                consonant_sequence += 1
                if consonant_sequence > 4:
                    failed_checks += 1
                    break
            else:
                consonant_sequence = 0
                
        if len(word) >= 4:
            char_counts = {}
            for char in word:
                char_counts[char] = char_counts.get(char, 0) + 1

            deviation = 0
            for char, count in char_counts.items():
                if char in LETTER_FREQUENCY:
                    expected = LETTER_FREQUENCY[char] / 100
                    actual = count / len(word)
                    deviation += abs(expected - actual)

            if (deviation / len(char_counts)) > 0.5:
                failed_checks += 1
                
        invalid_pairs = 0
        for i in range(len(word) - 1):
            pair = word[i:i+2]
            if pair not in VALID_PAIRS and pair[0] not in VOWELS and pair[1] not in VOWELS:
                invalid_pairs += 1
                if invalid_pairs > 1:
                    failed_checks += 1
                    break

        return failed_checks >= 2
            
    def check_all(self) -> list[CommitIssue]:
        self._run_gibberish_check()
        return self.issues
from typing import Tuple

class TextUtils:
    """Utility methods for separating and recombining letters/punctuation."""

    @staticmethod
    def seperateLettersPunctuation(text: str) -> Tuple[str, str]:
        """Separate alphabetic characters from punctuation, storing positions."""
        letters = ""
        punctuation = ""
        i = 0
        for char in text:
            if char.isalpha():
                letters += char
                i += 1
            else:
                punctuation += str(i) if i > 0 else ""
                punctuation += char
                i = 0
        return letters, punctuation
    
    @staticmethod
    def combineLettersPunctuation(letters: str, punctuation: str) -> str:
        """Recombine letters and punctuation based on encoded numeric positions."""
        text = ""
        start = 0
        end = 0
        for c in punctuation:
            if c.isdigit():
                end += int(c)
                text += letters[start:end]
                start = end
                continue
            text += c
        return text

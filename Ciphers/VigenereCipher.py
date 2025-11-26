from Ciphers.Cipher import Cipher
from TextUtils.AlphaChar import AlphaChar
from TextUtils.TextUtils import TextUtils

class VigenereCipher(Cipher):
    """Classic Vigenère Cipher implementation."""

    def __init__(self, key: str) -> None:
        self.key = key.upper()

    def encrypt(self, plaintext: str) -> str:
        """Encrypt text with Vigenère cipher."""
        ciphertext = ""
        letters, punctuation = TextUtils.seperateLettersPunctuation(plaintext)

        for i, char in enumerate(letters):
            cipherChar = AlphaChar(char)
            cipherChar += AlphaChar(self.key[i % len(self.key)])
            ciphertext += str(cipherChar)
        
        return TextUtils.combineLettersPunctuation(ciphertext, punctuation)

    def decrypt(self, ciphertext: str) -> str:
        """Decrypt text with Vigenère cipher."""
        plaintext = ""
        letters, punctuation = TextUtils.seperateLettersPunctuation(ciphertext)

        for i, char in enumerate(letters):
            plainChar = AlphaChar(char)
            plainChar -= AlphaChar(self.key[i % len(self.key)])
            plaintext += plainChar
        
        return TextUtils.combineLettersPunctuation(plaintext, punctuation)

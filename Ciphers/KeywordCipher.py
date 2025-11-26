import string
from Ciphers.Cipher import Cipher

class KeywordCipher(Cipher):
    """Implements a simple keyword substitution cipher."""

    def __init__(self, keyword: str) -> None:
        formattedKeyword = self.formatKeyword(keyword.upper())
        self.__alphabet = string.ascii_uppercase
        # Cipher alphabet: keyword followed by remaining letters
        self.__cipher_alpha = formattedKeyword + "".join(
            sorted(set(self.__alphabet) - set(formattedKeyword))
        )
    
    def formatKeyword(self, keyword: str) -> str:
        """Removes duplicate letters from keyword while preserving order."""
        formattedKeyword = ""
        for c in keyword:
            if c not in formattedKeyword:
                formattedKeyword += c
        return formattedKeyword
    
    def encrypt(self, plaintext: str) -> str:
        """Encrypts plaintext using the keyword substitution cipher."""
        ciphertext = ""
        for c in plaintext:
            if not c.isalpha():
                ciphertext += c
                continue
            if c.islower():
                cipherChar = self.__cipher_alpha.lower()[self.__alphabet.lower().index(c)]
            else:
                cipherChar = self.__cipher_alpha[self.__alphabet.index(c)]
            ciphertext += cipherChar
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """Decrypts ciphertext using the keyword substitution cipher."""
        plaintext = ""
        for c in ciphertext:
            if not c.isalpha():
                plaintext += c
                continue
            if c.islower():
                plainChar = self.__alphabet.lower()[self.__cipher_alpha.lower().index(c)]
            else:
                plainChar = self.__alphabet[self.__cipher_alpha.index(c)]
            plaintext += plainChar
        return plaintext

from Ciphers.Cipher import Cipher
from TextUtils.AlphaChar import AlphaChar
from TextUtils.TextUtils import TextUtils

class VigenereCipher(Cipher):
    def __init__(self, key):
        self.key = key.upper()

    def encrypt(self, plaintext):
        ciphertext = ""
        letters, puncuation = TextUtils.seperateLettersPunctuation(plaintext)
        for i, char in enumerate(letters):
            cipherChar = AlphaChar(char)
            cipherChar += AlphaChar(self.key[i%len(self.key)])
            
            ciphertext += str(cipherChar)
        
        return TextUtils.combineLettersPunctuation(ciphertext, puncuation)

    def decrypt(self, ciphertext):
        plaintext = ""
        letters, puncuation = TextUtils.seperateLettersPunctuation(ciphertext)
        for i, char in enumerate(letters):
            plainChar = AlphaChar(char)
            plainChar -= AlphaChar(self.key[i%len(self.key)])
            
            plaintext += plainChar
        
        return TextUtils.combineLettersPunctuation(plaintext, puncuation)
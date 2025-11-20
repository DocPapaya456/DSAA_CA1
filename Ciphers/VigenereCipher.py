from Ciphers.Cipher import Cipher

class VigenereCipher(Cipher):
    def __init__(self, key):
        self.key = key.upper()
    
    def seperateLettersPunctuation(self, text):
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

    def combineLettersPunctuation(self, letters, punctuation):
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

    def encrypt(self, plaintext):
        ciphertext = ""
        letters, puncuation = self.seperateLettersPunctuation(plaintext)
        for i, char in enumerate(letters):
            cipherChar = chr(ord('A') + (ord(char.upper()) + ord(self.key[i%len(self.key)]) - 2*ord('A')) % 26)
            if char.islower():
                cipherChar = cipherChar.lower()
            
            ciphertext += cipherChar
        
        return self.combineLettersPunctuation(ciphertext, puncuation)

    def decrypt(self, ciphertext):
        plaintext = ""
        letters, puncuation = self.seperateLettersPunctuation(ciphertext)
        for i, char in enumerate(letters):
            plainChar = chr(ord('A') + (ord(char.upper()) - ord(self.key[i%len(self.key)])) % 26)
            if char.islower():
                plainChar = plainChar.lower()
            
            plaintext += plainChar
        
        return self.combineLettersPunctuation(plaintext, puncuation)
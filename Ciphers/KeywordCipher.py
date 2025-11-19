import string

class KeywordCipher:
    def __init__(self, keyword):
        formattedKeyword = self.formatKeyword(keyword.upper())
        self.__alphabet = string.ascii_uppercase
        self.__cipher_alpha = formattedKeyword + "".join(sorted(set(self.__alphabet) - set(formattedKeyword)))
    
    # Removes duplicate letters in keyword
    def formatKeyword(self, keyword):
        formattedKeyword = ""
        for c in keyword:
            if not (c in formattedKeyword):
                formattedKeyword += c
        return formattedKeyword
    
    # Encrypts plaintext using keyword alphabet
    def encrypt(self, plaintext):
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
    
    # Decrypts ciphertext using keyword alphabet
    def decrypt(self, ciphertext):
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
    
    # Encrypts file contents from input_path and outputs into output_path
    def encryptFile(self, input_path, output_path):

        # Read from input file
        with open(input_path, 'r', encoding='utf-8') as infile:
            contents = infile.read()

        # Encrypt file contents
        processed = self.encrypt(contents)

        # Write processed data to output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed)

    # Decrypts file contents from input_path and outputs into output_path
    def decryptFile(self, input_path, output_path):
        # Read from input file
        with open(input_path, 'r', encoding='utf-8') as infile:
            contents = infile.read()

        # Encrypt file contents
        processed = self.decrypt(contents)

        # Write processed data to output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed)
from Ciphers.KeywordCipher import KeywordCipher
from LetterFrequency.LetterFrequency import LetterFrequency
from Ciphers.CipherInferer import CipherInferer
from Ciphers.VigenereCipher import VigenereCipher
import os

class Options:
    def __init__(self):
        self.__options = {
            "1": self.encyptDecryptFile,
            "2": self.displayLetterDistribution,
            "3": self.inferCipherKeyword,
            "4": self.batchDecryption,
            "5": self.encryptDecryptFileVignere,
            "6": self.extraTwo
        }

    # Runs specified option function
    def runOption(self, option):
        self.__options[option]()

    # Encrypt/Decrypt File
    def encyptDecryptFile(self):
        encryptOption = input('Enter "E" for Encrypt or "D" for Decrypt: ').strip().upper()
        print()
        while encryptOption != "E" and encryptOption != "D":
            encryptOption = input('Invalid Input. Please enter "E" for Encrypt or "D" for Decrypt: ').strip().upper()
            print()
        
        if encryptOption == "E":
            input_file = input('Please enter the file you want to encrypt: ')
            print()
            while not os.path.isfile(input_file):
                input_file = input('File not found. Please enter the file you want to encrypt: ')
                print()

            keyword = input('Enter the keyword: ')
            print()
            while not keyword.isalpha():
                keyword = input('Invalid keyword. Enter the keyword: ')
                print()
            
            output_file = input('Please enter an output file: ')
            print()
            
            keywordCipher = KeywordCipher(keyword)

            keywordCipher.encryptFile(input_file, output_file)
        
        else:
            input_file = input('Please enter the file you want to decrypt: ')
            print()
            while not os.path.isfile(input_file):
                input_file = input('File not found. Please enter the file you want to decrypt: ')
                print()
            
            keyword = input('Enter the keyword: ')
            print()
            while not keyword.isalpha():
                keyword = input('Invalid keyword. Enter the keyword: ')
                print()
            
            output_file = input("Please enter an output file: ")

            keywordCipher = KeywordCipher(keyword)

            keywordCipher.decryptFile(input_file, output_file)
    
    # Letter frequency distribution
    def displayLetterDistribution(self):
        input_file = input('Please enter the file you want to analyze: ')
        print()

        while not os.path.isfile(input_file):
            input_file = input('File not found. Please enter the file you want to analyze: ')
            print()
        
        letterFreq = LetterFrequency()
        letterFreq.analyseFromFile(input_file)
        print(letterFreq.displayGraph())
        print()

    # Infer cipher keyword
    def inferCipherKeyword(self):
        input_file = input('Please enter the file you want to analyze: ')
        print()

        while not os.path.isfile(input_file):
            input_file = input('File not found. Please enter the file you want to analyze: ')
            print()
        
        keyword_file = input('Please enter the keyword file: ')
        print()

        while not os.path.isfile(keyword_file):
            keyword_file = input('File not found. Please enter the keyword file: ')
            print()
        
        inferred_keyword = CipherInferer.inferKeywordFromFile(input_file, keyword_file)
        print(f'The inferred keyword is: {inferred_keyword}')

        decrypt_option = input('Would you want to decrypt this file using this key? y/n: ')
        print()

        if decrypt_option.lower() == 'y':
            output_file = input('Please enter an output file: ')

            cipher = KeywordCipher(inferred_keyword)
            cipher.decryptFile(input_file, output_file)

    # Batch decryption
    def batchDecryption(self):
        input_directory = input('Please enter the folder name: ')
        print()

        while not os.path.isdir(input_directory):
            print('Folder not found. Please enter the folder name: ')
            print()
        
        keyword_file = input('Please enter the keyword file: ')
        print()
        while not os.path.isfile(keyword_file):
            keyword_file = input('File not found. Please enter the keyword file: ')
            print()
        
        CipherInferer.batchInferKeyword(input_directory, keyword_file)

        input('Press Enter, to continue...')
        print()


    # Extra option 1
    def encryptDecryptFileVignere(self):
        # Info about Vignere Cipher
        print('''*********************
*  Vigenère Cipher  *
*********************

The Vigenère cipher is a classic method of encrypting alphabetic text using a repeating keyword to shift letters. It’s essentially multiple Caesar ciphers applied in sequence, where each letter of the keyword determines how much the corresponding plaintext letter is shifted.

How it works:

1.  Choose a keyword (e.g., LEMON).

2.  Repeat the keyword to match the length of the plaintext.

3.  For each letter, shift the plaintext letter forward by the alphabetical index of the keyword letter (A=0, B=1, …).

4.  The result is the ciphertext.

Because it uses multiple shifting values instead of a single one, the Vigenère cipher is stronger than a simple Caesar cipher—though it can still be broken using methods like Kasiski examination, Friedman test, or chi-squared analysis once the keyword length is known.
''')
        input('Press Enter, to continue...')
        encryptOption = input('Enter "E" for Encrypt or "D" for Decrypt: ').strip().upper()
        print()
        while encryptOption != "E" and encryptOption != "D":
            encryptOption = input('Invalid Input. Please enter "E" for Encrypt or "D" for Decrypt: ').strip().upper()
            print()
        
        if encryptOption == "E":
            input_file = input('Please enter the file you want to encrypt: ')
            print()
            while not os.path.isfile(input_file):
                input_file = input('File not found. Please enter the file you want to encrypt: ')
                print()

            keyword = input('Enter the keyword: ')
            print()
            while not keyword.isalpha():
                keyword = input('Invalid keyword. Enter the keyword: ')
                print()
            
            output_file = input('Please enter an output file: ')
            print()
            
            vignereCipher = VigenereCipher(keyword)

            vignereCipher.encryptFile(input_file, output_file)
        
        else:
            input_file = input('Please enter the file you want to decrypt: ')
            print()
            while not os.path.isfile(input_file):
                input_file = input('File not found. Please enter the file you want to decrypt: ')
                print()
            
            keyword = input('Enter the keyword: ')
            print()
            while not keyword.isalpha():
                keyword = input('Invalid keyword. Enter the keyword: ')
                print()
            
            output_file = input("Please enter an output file: ")

            vignereCipher = VigenereCipher(keyword)

            vignereCipher.decryptFile(input_file, output_file)
    
    # Extra option 2
    def extraTwo(self):
        print("extraTwo: Not implemented!")
from Ciphers.KeywordCipher import KeywordCipher
from LetterFrequency.LetterFrequency import LetterFrequency
import Ciphers.CipherInferer as CipherInferer
import os

class Options:
    def __init__(self):
        self.__options = {
            "1": self.encyptDecryptFile,
            "2": self.displayLetterDistribution,
            "3": self.inferCipherKeyword,
            "4": self.batchDecryption,
            "5": self.extraOne,
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
    def extraOne(self):
        print("extraOne: Not implemented!")
    
    # Extra option 2
    def extraTwo(self):
        print("extraTwo: Not implemented!")
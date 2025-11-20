from Ciphers.KeywordCipher import KeywordCipher
from LetterFrequency.LetterFrequency import LetterFrequency
from DataStructures.SortedList import SortedList
from Ciphers.FileNode import FileNode
import os

class CipherInferer:
    @staticmethod
    def inferKeyword(ciphertext, keywords):
        minChiSquared = float('inf')
        bestKeyword = None
        for keyword in keywords:
            cipher = KeywordCipher(keyword)
            plaintext = cipher.decrypt(ciphertext)
            frequency = LetterFrequency()
            frequency.analyseFrequency(plaintext)
            chiSquared = frequency.calculateChiSquared()
            if chiSquared < minChiSquared:
                minChiSquared = chiSquared
                bestKeyword = keyword
        
        return bestKeyword

    @staticmethod
    def inferKeywordFromFile(input_file, keyword_file):
        with open(input_file, 'r', encoding='utf-8') as infile:
            ciphertext = infile.read()
        
        with open(keyword_file, 'r', encoding='utf-8') as infile:
            keywords = [keyword.rstrip() for keyword in infile.readlines()]

        return CipherInferer.inferKeyword(ciphertext, keywords)
    
    @staticmethod
    def batchInferKeyword(input_directory, keyword_file):
        files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]
        fileList = SortedList()
        for file in files:
            inferredKeyword = CipherInferer.inferKeywordFromFile(file, keyword_file)
            fileList.insert(FileNode(file, inferredKeyword))
        fileList = fileList.toList()

        logtext = ""
        for i, fileNode in enumerate(fileList):
            cipher = KeywordCipher(fileNode.keyword)
            cipher.decryptFile(fileNode.file, os.path.join(input_directory, f'file{i+1}.txt'))
            
            log = f'Decrypting: {os.path.basename(fileNode.file)} using keyword: {fileNode.keyword} as: file{i+1}.txt'
            print(log)
            print()
            logtext += log + '\n'
        
        with open(os.path.join(input_directory, 'log.txt'), 'w') as logfile:
            logfile.write(logtext)
    
        
        

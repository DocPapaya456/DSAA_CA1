from Ciphers.KeywordCipher import KeywordCipher
from LetterFrequency.LetterFrequency import LetterFrequency
from DataStructures.SortedList import SortedList
from Ciphers.FileNode import FileNode
import os
from typing import List, Optional

class CipherInferer:
    """Class providing utilities to infer cipher keywords via frequency analysis."""

    @staticmethod
    def inferKeyword(ciphertext: str, keywords: List[str]) -> Optional[str]:
        """Infer which keyword best fits a ciphertext using chi-squared analysis."""
        minChiSquared = float('inf')
        bestKeyword = None

        for keyword in keywords:
            cipher = KeywordCipher(keyword)
            plaintext = cipher.decrypt(ciphertext)

            # Analyze decrypted text frequency
            frequency = LetterFrequency()
            frequency.analyseFrequency(plaintext)
            chiSquared = frequency.calculateChiSquared()

            # Keep track of lowest chi-squared match
            if chiSquared < minChiSquared:
                minChiSquared = chiSquared
                bestKeyword = keyword
        
        return bestKeyword

    @staticmethod
    def inferKeywordFromFile(input_file: str, keyword_file: str) -> Optional[str]:
        """Infer keyword from ciphertext and list of possible keywords."""
        with open(input_file, 'r', encoding='utf-8') as infile:
            ciphertext = infile.read()
        
        with open(keyword_file, 'r', encoding='utf-8') as infile:
            keywords = [keyword.rstrip() for keyword in infile.readlines()]

        return CipherInferer.inferKeyword(ciphertext, keywords)
    
    @staticmethod
    def batchInferKeyword(input_directory: str, keyword_file: str) -> None:
        """Batch inference: decrypt and log multiple files in a folder."""
        files = [
            os.path.join(input_directory, f)
            for f in os.listdir(input_directory)
            if os.path.isfile(os.path.join(input_directory, f))
        ]

        fileList = SortedList()
        for file in files:
            inferredKeyword = CipherInferer.inferKeywordFromFile(file, keyword_file)
            fileList.insert(FileNode(file, inferredKeyword))

        fileList = fileList.toList()
        logtext = ""

        # Decrypt each file and keep log
        for i, fileNode in enumerate(fileList):
            cipher = KeywordCipher(fileNode.keyword)
            cipher.decryptFile(fileNode.file, os.path.join(input_directory, f'file{i+1}.txt'))
            
            log = f'Decrypting: {os.path.basename(fileNode.file)} using keyword: {fileNode.keyword} as: file{i+1}.txt'
            print(log)
            print()
            logtext += log + '\n'
        
        with open(os.path.join(input_directory, 'log.txt'), 'w') as logfile:
            logfile.write(logtext)

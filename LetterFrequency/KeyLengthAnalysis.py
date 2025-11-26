from Graph.BarGraph import BarGraph
from TextUtils.TextUtils import TextUtils
import string
import math
from LetterFrequency.IOCNode import IOCNode
from DataStructures.SortedList import SortedList


class KeyLengthAnalysis(BarGraph):

    def __init__(self):
        super().__init__()
        self.distribution = SortedList()
    
    # Analyses letter frequency from file content
    def analyseFromFile(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as infile:
            contents = infile.read()
        
        self.analyseCiphertext(contents)
    
    def analyseCiphertext(self, ciphertext):
        cipherLetters, _ = TextUtils.seperateLettersPunctuation(ciphertext)
        for i in range(9):
            columns = [cipherLetters[j::i+1] for j in range(i+1)]
            columnIOC = [self.calculateIOC(column) for column in columns]
            avgIOC = sum(columnIOC)/len(columnIOC)
            self.distribution.insert(IOCNode(i+1, avgIOC))
    
    def calculateIOC(self, text):
        counts = [0] * 26
        totalChars = len(text)
        for char in text.upper():
            counts[string.ascii_uppercase.index(char)] += 1

        counts = [26 * count * (count-1) / (totalChars * (totalChars-1)) for count in counts]
        ioc = sum(counts)
        return ioc

    def calculateNoOfStars(self, frequency):
        return 0 if frequency == 0 else int(math.floor(frequency/max(self.distribution).IOC * 10) + 1)
    
    def addInformation(self):
        formattedIOCs = self.__formatIOCs()
        for i in range(len(formattedIOCs)):
            self.graph[i] += formattedIOCs[i]
        self.__formatTopIOCs()

    def __formatTopIOCs(self):
        # Add padding
        for i in range(4, 9):
            self.graph[i] += "    "
        
        self.graph[4] += "TOP 3 IOC"
        self.graph[5] += "----------"

        top3 = self.distribution.top(3)

        for i in range(6, 9):
            self.graph[i] += f'| {top3[i-6].num}-{top3[i-6].IOC:5.2f}'
        




    def __formatIOCs(self):
        return [f'{i+1}-{node.IOC:5.2f}' for i, node in enumerate(self.distribution)]
    
    def displayGraph(self):
        IOCList = self.distribution.toList()
        heights = [0] * len(IOCList)
        for node in IOCList:
            heights[node.num-1] = node.IOC
        self.plot(9, [str(n) for n in range(1, self.distribution.size() + 1)], heights)

        


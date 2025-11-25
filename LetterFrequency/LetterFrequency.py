from DataStructures.SortedList import SortedList
from LetterFrequency.FreqNode import FreqNode
import string
from Graph.BarGraph import BarGraph

class LetterFrequency(BarGraph):
    def __init__(self):
        super().__init__()
        # Track two lists: one sorted by frequency, another sorted by alphabetical order
        self.frequencyList = SortedList()
        self.letterList = SortedList()
        self.numLetters = 0

    # Analyses letter frequency from file content
    def analyseFromFile(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as infile:
            contents = infile.read()
        
        self.analyseFrequency(contents)

    # Stores frequency of each letter into FreqNodes and sorted using SortedLists    
    def analyseFrequency(self, text):
        formatted = ""
        for c in text:
            if c.isalpha():
                formatted += c
        
        formatted = formatted.upper()
        self.numLetters = len(formatted)

        frequencies = {c: 0 for c in string.ascii_uppercase}

        for c in set(formatted):
            frequencies[c] = (formatted.count(c) / self.numLetters) * 100
        
        for c, frequency in frequencies.items():
            self.__insertLetterFrequency(c, frequency)

    # Override displayGraph to include frequencies into graph
    def displayGraph(self):
        self.plot(list(string.ascii_uppercase), [node.frequency for node in self.letterList.toList()])
    
    # Function to insert letter frequency into both lists
    def __insertLetterFrequency(self, letter, frequency):
        self.frequencyList.insert(FreqNode(letter, frequency))
        self.letterList.insert(FreqNode(letter, frequency, sortType='letter'))

    # Override addInformation to add top frequencies
    def addInformation(self):
        formattedFrequencies = self.__formatLetterFrequencies()
        self.graph = [self.graph[i] + formattedFrequencies[i] for i in range(len(self.graph))]
        self.__formatTopFreqencies()
    
    # Creates list of letter frequencies
    def __formatLetterFrequencies(self):
        return [f'{node.letter}-{node.frequency:5.2f}%' for node in self.letterList.toList()]
    
    # Creates Top 5 frequencies list
    def __formatTopFreqencies(self):
        # Add padding
        for i in range(10, 17):
            self.graph[i] += "    "
        
        self.graph[10] += "TOP 5 FREQ"
        self.graph[11] += "----------"

        freqList = self.frequencyList.top(5)

        for i in range(12, 17):
            self.graph[i] += f'| {freqList[i-12].letter}-{freqList[i-12].frequency:5.2f}%'
        

    # Calculate chi-squared statistic of analysed text
    def calculateChiSquared(self):
        with open('LetterFrequency/english_letter_frequency.txt', 'r') as f:
            expectedFrequency = [float(line.split(',')[1]) for line in f.readlines()]
        
        frequencyList = self.letterList.toList()

        chi_squared = self.numLetters * sum([((o.frequency - e)**2)/e for o, e in zip(frequencyList, expectedFrequency)])
        
        return float(chi_squared)





            
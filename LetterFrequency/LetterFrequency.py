from DataStructures.SortedList import SortedList
from LetterFrequency.FreqNode import FreqNode
import string

class LetterFrequency:
    def __init__(self):
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
    
    # Function to insert letter frequency into both lists
    def __insertLetterFrequency(self, letter, frequency):
        self.frequencyList.insert(FreqNode(letter, frequency))
        self.letterList.insert(FreqNode(letter, frequency, sortType='letter'))
    
    # Displays distribution graph
    def displayGraph(self):
        if self.frequencyList.empty():
            print('LetterFrequency: No analysis has been done! Please analyse text before displaying graph.')
            return
        
        barGraph = self.__buildLetterBarGraph()
        barGraph = self.__reformatBarGraph(barGraph)
        formattedFrequencies = self.__formatLetterFrequencies()
        barGraph = [barGraph[i] + formattedFrequencies[i] for i in range(len(barGraph))]
        barGraph = self.__formatTopFreqencies(barGraph)
        barGraph.append("_____________________________________________________|")
        barGraph.append(" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  ")

        return "\n".join(barGraph)

    # Rotates bar graph anti-clockwise
    def __reformatBarGraph(self, barGraph):
        return [" " + " ".join([string[-i] for string in barGraph]) + " " for i in range(1, len(barGraph[0]) + 1)]

    # Create strings of stars for each letter    
    def __buildLetterBar(self, frequency):
        return f"{'*'*self.__calculateNoOfStars(frequency):<26}"
    
    # Combines strings of stars together into a list
    def __buildLetterBarGraph(self):
        return [self.__buildLetterBar(node.frequency) for node in self.letterList.toList()]

    # Calculates correct number of stars for each letter
    def __calculateNoOfStars(self, frequency):
        return 0 if frequency == 0 else int(((frequency * 26) // 100) + 1)
    
    # Creates list of letter frequencies
    def __formatLetterFrequencies(self):
        return [f'| {node.letter}-{node.frequency:5.2f}%' for node in self.letterList.toList()]
    
    # Creates Top 5 frequencies list
    def __formatTopFreqencies(self, barGraph):
        # Add padding
        for i in range(10, 17):
            barGraph[i] += "    "
        
        barGraph[10] += "TOP 5 FREQ"
        barGraph[11] += "----------"

        freqList = self.frequencyList.top(5)

        for i in range(12, 17):
            barGraph[i] += f'| {freqList[i-12].letter}-{freqList[i-12].frequency:5.2f}%'
        
        return barGraph

    # Calculate chi-squared statistic of analysed text
    def calculateChiSquared(self):
        if self.frequencyList.empty():
            print('LetterFrequency: No analysis has been done! Please analyse text before calculating chi-squared.')
            return

        with open('LetterFrequency/english_letter_frequency.txt', 'r') as f:
            expectedFrequency = [float(line.split(',')[1]) for line in f.readlines()]
        
        frequencyList = self.letterList.toList()

        chi_squared = self.numLetters * sum([((o.frequency - e)**2)/e for o, e in zip(frequencyList, expectedFrequency)])
        
        return float(chi_squared)





            
from DataStructures.SortedList import SortedList
from LetterFrequency.FreqNode import FreqNode
import string
from Graph.BarGraph import BarGraph

class LetterFrequency(BarGraph):
    """Analyzes and visualizes letter frequencies in a text."""

    def __init__(self) -> None:
        super().__init__()
        self.frequencyList = SortedList()  # Sort by frequency
        self.letterList = SortedList()     # Sort alphabetically
        self.numLetters: int = 0

    def analyseFromFile(self, filepath: str) -> None:
        """Analyze letter frequencies in a text file."""
        with open(filepath, 'r', encoding='utf-8') as infile:
            contents = infile.read()
        self.analyseFrequency(contents)
    
    def analyseFrequency(self, text: str) -> None:
        """Analyze frequencies of letters within given string."""
        formatted = "".join(c for c in text if c.isalpha()).upper()
        self.numLetters = len(formatted)

        frequencies = {c: 0 for c in string.ascii_uppercase}
        for c in set(formatted):
            frequencies[c] = (formatted.count(c) / self.numLetters) * 100 if self.numLetters else 0
        
        for c, frequency in frequencies.items():
            self.__insertLetterFrequency(c, frequency)

    def displayGraph(self) -> None:
        """Display letter frequency graph in console."""
        self.plot(26, list(string.ascii_uppercase), [node.frequency for node in self.letterList.toList()])
    
    def __insertLetterFrequency(self, letter: str, frequency: float) -> None:
        """Insert frequency data into both lists."""
        self.frequencyList.insert(FreqNode(letter, frequency))
        self.letterList.insert(FreqNode(letter, frequency, sortType='letter'))
    
    def calculateNoOfStars(self, frequency: float) -> int:
        """Convert frequency to proportional star count."""
        return 0 if frequency == 0 else int(((frequency * 26) // 100) + 1)

    def addInformation(self) -> None:
        """Add frequency percentage details and top 5 letters beside graph."""
        formattedFrequencies = self.__formatLetterFrequencies()
        self.graph = [self.graph[i] + formattedFrequencies[i] for i in range(len(self.graph))]
        self.__formatTopFrequencies()
    
    def __formatLetterFrequencies(self) -> list[str]:
        """Format letter-frequency info for display next to bars."""
        return [f'{node.letter}-{node.frequency:5.2f}%' for node in self.letterList.toList()]
    
    def __formatTopFrequencies(self) -> None:
        """Display top 5 most frequent letters on the right side of graph."""
        for i in range(10, 17):
            self.graph[i] += "    "
        
        self.graph[10] += "TOP 5 FREQ"
        self.graph[11] += "----------"

        freqList = self.frequencyList.top(5)
        for i in range(12, 17):
            self.graph[i] += f'| {freqList[i-12].letter}-{freqList[i-12].frequency:5.2f}%'
    
    def calculateChiSquared(self) -> float:
        """Compute Chi-squared statistic comparing with English letter distribution."""
        with open('LetterFrequency/english_letter_frequency.txt', 'r', encoding='utf-8') as f:
            expectedFrequency = [float(line.split(',')[1]) for line in f.readlines()]
        
        frequencyList = self.letterList.toList()
        chi_squared = self.numLetters * sum([((o.frequency - e)**2)/e for o, e in zip(frequencyList, expectedFrequency)])
        return float(chi_squared)

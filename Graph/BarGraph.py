from abc import ABC, abstractmethod
class BarGraph(ABC):
    def __init__(self):
        self.graph = None
    
    # Formats the graph
    def buildGraph(self, labels, heights):
        self.graph = self.__buildBarGraph(heights)
        self.graph = self.__reformatBarGraph()
        self.addInformation()
        labelsAxis = ' ' + ' '.join(labels) + '  '
        self.graph.append('_' * (len(labelsAxis)-1))
        self.graph.append(labelsAxis)
    
    # Rotates bar graph anti-clockwise
    def __reformatBarGraph(self):
        return [' ' + ' '.join([string[-i] for string in self.graph]) + ' |' for i in range(1, len(self.graph[0]) + 1)]

    # Create strings of stars for each bar   
    def __buildBar(self, frequency):
        return f"{'*'*self.__calculateNoOfStars(frequency):<26}"
    
    # Combines strings of stars together into a list
    def __buildBarGraph(self, heights):
        return [self.__buildBar(height) for height in heights]

    # Calculates correct number of stars for each bar
    def __calculateNoOfStars(self, frequency):
        return 0 if frequency == 0 else int(((frequency * 26) // 100) + 1)
    
    # Prints formatted graph to command line
    def plot(self, labels, heights):
        self.buildGraph(labels, heights)
        print("\n".join(self.graph))
    
    # Method to supply labels and heights and display graph
    @abstractmethod
    def displayGraph(self):
        pass
    
    # Method to include additional information in the graph
    @abstractmethod
    def addInformation(self):
        pass

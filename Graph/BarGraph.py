from abc import ABC, abstractmethod
from typing import List

class BarGraph(ABC):
    """Base class for drawing ASCII bar graphs."""

    def __init__(self) -> None:
        self.graph: List[str] = []
        self.labels: List[str] = []
        self.height: int = 0
    
    def buildGraph(self, labels: List[str], heights: List[float]) -> None:
        """Constructs the bar graph layout from labels and heights."""
        self.labels = labels
        self.graph = self.__buildBarGraph(heights)
        self.graph = self.__reformatBarGraph()
        self.addInformation()
        labelsAxis = ' ' + ' '.join(labels) + '  '
        self.graph.append('_' * (len(labelsAxis)-1))
        self.graph.append(labelsAxis)
    
    def __reformatBarGraph(self) -> List[str]:
        """Rotates bars anti-clockwise for vertical display."""
        return [' ' + ' '.join([string[-i] for string in self.graph]) + ' |' for i in range(1, len(self.graph[0]) + 1)]

    def buildBar(self, frequency: float) -> str:
        """Create one vertical bar of stars based on frequency."""
        return "{:<{strLength}}".format('*' * self.calculateNoOfStars(frequency), strLength=self.height)
    
    def __buildBarGraph(self, heights: List[float]) -> List[str]:
        """Build horizontal list of bar strings."""
        return [self.buildBar(height) for height in heights]
    
    def plot(self, graphHeight: int, labels: List[str], heights: List[float]) -> None:
        """Plot the graph to terminal."""
        self.height = graphHeight
        self.buildGraph(labels, heights)
        print("\n".join(self.graph))

    @abstractmethod
    def calculateNoOfStars(self, frequency: float) -> int:
        """Return number of stars to represent given frequency."""
        pass

    @abstractmethod
    def displayGraph(self) -> None:
        """Display the complete bar graph."""
        pass

    @abstractmethod
    def addInformation(self) -> None:
        """Add extra information to the graph display."""
        pass

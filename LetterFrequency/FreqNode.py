from DataStructures.Node import Node
from typing import Optional

class FreqNode(Node):
    """Represents a single letter with its frequency for sorting."""

    def __init__(self, letter: str, frequency: float, sortType: str = 'frequency') -> None:
        if sortType not in ['frequency', 'letter']:
            raise ValueError("FreqNode: sortType must be either 'frequency' or 'letter'.")
        super().__init__()
        self.letter = letter.upper()
        self.frequency = frequency
        self.sortType = sortType

    def __eq__(self, otherNode: Optional["FreqNode"]) -> bool:
        """Compare equality by frequency and letter."""
        if otherNode is None:
            return False
        return self.frequency == otherNode.frequency and self.letter == otherNode.letter

    def __lt__(self, otherNode: Optional["FreqNode"]) -> bool:
        """Compare order for sorting depending on sortType."""
        if otherNode is None:
            raise TypeError("'<' not supported between instances of 'FreqNode' and 'NoneType'")
        
        if self.sortType == 'frequency':
            # When frequencies are equal, compare alphabetically (reverse for descending)
            if self.frequency == otherNode.frequency:
                return self.letter > otherNode.letter
            return self.frequency < otherNode.frequency
        
        return self.letter < otherNode.letter

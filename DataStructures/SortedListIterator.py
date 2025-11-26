from DataStructures.Node import Node
from typing import Optional, Iterator

class SortedListIterator:
    """Iterator class for traversing SortedList."""

    def __init__(self, head: Optional[Node]) -> None:
        self.current: Optional[Node] = head

    def __iter__(self) -> "SortedListIterator":
        return self
    
    def __next__(self) -> Node:
        if self.current is None:
            raise StopIteration
        
        current = self.current
        self.current = self.current.nextNode
        return current

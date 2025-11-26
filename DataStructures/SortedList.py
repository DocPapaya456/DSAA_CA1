from DataStructures.SortedListIterator import SortedListIterator
from DataStructures.Node import Node
from typing import List, Optional

class SortedList:
    """Linked list that maintains sorted order of inserted nodes."""

    def __init__(self) -> None:
        self.headNode: Optional[Node] = None
    
    def empty(self) -> bool:
        """Check if the list is empty."""
        return self.headNode is None
    
    def insert(self, node: Node) -> None:
        """Insert a new node while maintaining sorted order."""
        if self.empty() or node < self.headNode:
            node.nextNode = self.headNode
            self.headNode = node
            return
        
        current = self.headNode
        while current.nextNode and node > current.nextNode:
            current = current.nextNode
        
        if current.nextNode is None:
            current.nextNode = node
            return
        
        node.nextNode = current.nextNode
        current.nextNode = node

    def size(self) -> int:
        """Count number of nodes in list."""
        count = 0
        current = self.headNode
        while current:
            count += 1
            current = current.nextNode
        return count
    
    def top(self, n: int) -> List[Node]:
        """Return top 'n' nodes (sorted descending)."""
        if self.empty():
            return []
        current = self.headNode
        topNodes = [self.headNode]
        while current.nextNode:
            topNodes.append(current.nextNode)
            if len(topNodes) > n:
                topNodes.pop(0)
            current = current.nextNode
        return topNodes[::-1]
    
    def __str__(self) -> str:
        if self.empty():
            return '<>'
        nodes = []
        current = self.headNode
        while current:
            nodes.append(current)
            current = current.nextNode
        return "<" + ",".join([str(node) for node in nodes]) + ">"
    
    def toList(self) -> List[Node]:
        """Convert linked list to a regular Python list."""
        result = []
        current = self.headNode
        while current:
            result.append(current)
            current = current.nextNode
        return result
    
    def __iter__(self) -> SortedListIterator:
        """Return an iterator for the list."""
        return SortedListIterator(self.headNode)

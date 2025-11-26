from DataStructures.Node import Node
from typing import Optional

class IOCNode(Node):
    """Stores number (key length hypothesis) and IOC value."""

    def __init__(self, num: int, IOC: float) -> None:
        super().__init__()
        self.num = num
        self.IOC = IOC

    def __eq__(self, otherNode: Optional["IOCNode"]) -> bool:
        if otherNode is None:
            return False
        return self.IOC == otherNode.IOC
    
    def __lt__(self, otherNode: Optional["IOCNode"]) -> bool:
        if otherNode is None:
            raise TypeError("'<' not supported between instances of 'IOCNode' and 'NoneType'")
        return self.IOC < otherNode.IOC

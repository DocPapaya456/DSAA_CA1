from DataStructures.Node import Node
from typing import Optional

class FileNode(Node):
    """Node storing a file path and its inferred keyword for sorting."""

    def __init__(self, file: str, keyword: str) -> None:
        super().__init__()
        self.file = file
        self.keyword = keyword
    
    def __eq__(self, otherNode: Optional["FileNode"]) -> bool:
        if otherNode is None:
            return False
        return self.keyword == otherNode.keyword
    
    def __lt__(self, otherNode: Optional["FileNode"]) -> bool:
        if otherNode is None:
            raise TypeError("'<' not supported between instances of 'FileNode' and 'NoneType'")
        return self.keyword < otherNode.keyword

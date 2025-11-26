from abc import ABC, abstractmethod
from typing import Optional, Any

class Node(ABC):
    """Abstract base class representing a node in a linked structure."""

    def __init__(self) -> None:
        self.nextNode: Optional["Node"] = None

    @abstractmethod
    def __lt__(self, otherNode: Any) -> bool:
        """Compare this node with another (less than)."""
        pass

    @abstractmethod
    def __eq__(self, otherNode: Any) -> bool:
        """Check if this node equals another."""
        pass

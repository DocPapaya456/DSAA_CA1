from abc import ABC, abstractmethod
class Node(ABC):
    def __init__(self):
        self.nextNode = None

    @abstractmethod
    def __lt__(self, otherNode):
        pass

    @abstractmethod
    def __eq__(self, otherNode):
        pass

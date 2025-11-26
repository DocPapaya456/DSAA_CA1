from DataStructures.Node import Node
class SortedListIterator:
    def __init__(self, head : Node):
        self.current = head

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        
        current = self.current
        self.current = self.current.nextNode
        return current
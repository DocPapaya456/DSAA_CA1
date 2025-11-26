from DataStructures.Node import Node

class FreqNode(Node):
    def __init__(self, letter, frequency, sortType = 'frequency'):
        if sortType not in ['frequency', 'letter']:
            raise ValueError("FreqNode: sortType must be either 'frequency' or 'letter'.")

        super().__init__()
        self.letter = letter.upper()
        self.frequency = frequency
        self.sortType = sortType

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        return self.frequency == otherNode.frequency and self.letter == otherNode.letter

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'FreqNode' and 'NoneType'")
        
        if self.sortType == 'frequency':
        
            if self.frequency == otherNode.frequency:
                return self.letter > otherNode.letter
            
            return self.frequency < otherNode.frequency
        
        return self.letter < otherNode.letter
    
    # def __repr__(self):
    #     return f"{self.letter}: {self.frequency:.2f}%"
from DataStructures.Node import Node

class IOCNode(Node):
    def __init__(self, num, IOC):
        super().__init__()
        self.num = num
        self.IOC = IOC

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        return self.IOC == otherNode.IOC
    
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'IOCNode' and 'NoneType'")
        
        return self.IOC < otherNode.IOC
    
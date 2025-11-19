from DataStructures.Node import Node
class FileNode(Node):
    def __init__(self, file, keyword):
        super().__init__()
        self.file = file
        self.keyword = keyword
    
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        return self.keyword == otherNode.keyword
    
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'FileNode' and 'NoneType'")
        return self.keyword < otherNode.keyword
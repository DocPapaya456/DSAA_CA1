class SortedList:
    def __init__(self):
        self.headNode = None
    
    def empty(self):
        return self.headNode == None
    
    def insert(self, node):

        if self.empty() or node < self.headNode:
            node.nextNode = self.headNode
            self.headNode = node
            return
        
        current = self.headNode

        while current.nextNode and node > current.nextNode:
            current = current.nextNode
        
        if current.nextNode == None:
            current.nextNode = node
            return
        
        node.nextNode = current.nextNode
        current.nextNode = node

    def size(self):
        if self.empty():
            return 0
        
        current = self.headNode
        count = 0
        while current != None:
            count += 1
            current = current.nextNode
        
        return count
    
    def top(self, n):
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
    
    def __str__(self):
        if self.empty():
            return '<>'
        
        current = self.headNode
        nodes = [self.headNode]

        while current.nextNode:
            nodes.append(current.nextNode)
            current = current.nextNode
        
        return "<" + ",".join([str(node) for node in nodes]) + ">"
    
    def toList(self):
        if self.empty():
            return []
        
        result = [self.headNode]
        current = self.headNode

        while current.nextNode:
            result.append(current.nextNode)
            current = current.nextNode
        
        return result


        

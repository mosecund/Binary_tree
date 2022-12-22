
class BinaryTree:
    def __init__(self,rootVal,leftBinaryTree=None,rightBinaryTree=None):
        self.key = rootVal
        self.left = leftBinaryTree
        self.right = rightBinaryTree
    
    def getRootVal(self):
        return self.key

    def setRootVal(self,obj):
        self.key = obj

    def getLeftChild(self):
        return self.left

    def setLeftChild(self,leftChild):
        self.left = leftChild

    def getRightChild(self):
        return self.right
    
    def setRightChild(self,rightChild):
        self.right = rightChild
        
    def insert(self,value):
        if self.getRootVal() == None:
            self.setRootVal(value)
        elif value <= self.getRootVal():
            if self.getLeftChild() == None:
                self.setLeftChild(BinaryTree(value))
            else:
                self.getLeftChild().insert(value)
        else:
            if self.getRightChild() == None:
                self.setRightChild(BinaryTree(value))
            else:
                self.getRightChild().insert(value)
        
    def init_values(self,values):
        self.setLeftChild(None)
        self.setRightChild(None)
        self.setRootVal(None)
        for v in values:
            self.insert(v)

        
        
        
        

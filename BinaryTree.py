

class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def insertLeftChild(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tempNode = BinaryTree(newNode)
            tempNode.leftChild = self.leftChild
            self.leftChild = tempNode

    def getLeftChild(self):
        return self.leftChild

    def insertRightChild(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tempNode = BinaryTree(newNode)
            tempNode.rightChild = self.rightChild
            self.rightChild = tempNode

    def getRightChild(self):
        return self.rightChild




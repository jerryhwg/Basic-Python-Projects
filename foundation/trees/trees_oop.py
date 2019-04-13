# Python 3.7.2
# Trees with OOP
# Nodes and References Implementation


class BinaryTree(object):

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        
        if self.leftChild == None: # there is no child so simply add a node to that tree
            self.leftChild = BinaryTree(newNode)
        else: # there is an child so insert a node and push the existing child down one level in the tree
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode): # right child
        
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


"""

Test
r = BinaryTree('a')
r.getRootVal()
print(r.getLeftChild())
r.insertLeft('b')
r.getLeftChild().getRootVal()

"""
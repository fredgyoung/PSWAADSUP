from BinaryTree import BinaryTree

mytree = BinaryTree('a')
print(mytree.getRootVal())
print(mytree.getLeftChild())

mytree.insertLeftChild('b')
print(mytree.getLeftChild())

mytree.insertRightChild('c')
print(mytree.getRightChild())

print(mytree.getRightChild().getRootVal())
mytree.getRightChild().setRootVal('hello')
print(mytree.getRightChild().getRootVal())

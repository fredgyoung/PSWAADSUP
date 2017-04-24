from BinaryTree import BinaryTree

root = BinaryTree('a')
print(root.getRootVal())
print(root.getLeftChild())

root.insertLeftChild('b')
print(root.getLeftChild())

root.insertRightChild('c')
print(root.getRightChild())

print(root.getRightChild().getRootVal())
root.getRightChild().setRootVal('hello')
print(root.getRightChild().getRootVal())

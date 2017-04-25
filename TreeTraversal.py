from BinaryTree import BinaryTree

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

if __name__ == '__main__':
    mytree = BinaryTree('a')
    mytree.insertLeftChild('b')
    mytree.insertRightChild('c')
    mytree.getLeftChild().insertLeftChild('d')
    mytree.getLeftChild().insertRightChild('e')
    mytree.getRightChild().insertLeftChild('f')
    mytree.getRightChild().insertRightChild('g')

    preorder(mytree)
    print()
    postorder(mytree)
    print()
    inorder(mytree)


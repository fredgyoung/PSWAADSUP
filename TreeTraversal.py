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

def invert(tree):
    if tree:
        invert(tree.getLeftChild())
        invert(tree.getRightChild())
        if tree.leftChild and tree.rightChild:
            tree.leftChild, tree.rightChild = tree.rightChild, tree.leftChild


if __name__ == '__main__':
    mytree = BinaryTree(1)
    mytree.insertLeftChild(2)
    mytree.insertRightChild(3)
    mytree.getLeftChild().insertLeftChild(4)
    mytree.getLeftChild().insertRightChild(5)
    mytree.getRightChild().insertLeftChild(6)
    mytree.getRightChild().insertRightChild(7)

    preorder(mytree)
    print()
    invert(mytree)
    preorder(mytree)
    print()

#    postorder(mytree)
#    print()
#    inorder(mytree)


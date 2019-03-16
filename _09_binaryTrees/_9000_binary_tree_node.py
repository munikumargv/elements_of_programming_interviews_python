class BinaryTreeNode:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # supplementary code not from book
    def insert(self, data):
        # compare new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()


def tree_traversal(root):
    if root:
        # pre order: processes the root before the traversals of the left and right
        # children
        print('Pre-order: %d' % root.data)
        tree_traversal(root.left)

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def wrapper(root):

    def sum_leaves(node, res=0):
        if node is None:
            return 0

        if not node.left and not node.right:
            return node.value

        res += sum_leaves(node.left, res)
        return res + sum_leaves(node.right, res)

    return sum_leaves(root)

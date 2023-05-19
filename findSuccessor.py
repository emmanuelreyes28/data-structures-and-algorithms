# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


'''
In a tree's in-order traversale we follow these steps:
1. left
2. visit
3. right

Keep going left until reach leaf node. Add leaf node to array and make your
way back up the tree checkin if each node has a node to its right

To make the solution optimal we know that a node's successor is going to be the furthest
left node in that tree if it has a right subtree

No right subtree - when we are in a right child of a parent's node we know
that, that node cannot be the given nodes successor. Instead we have to go
further up the tree. A nodes successor must have came from a left child of a 
parent
'''
# O(h) time | O(1) space - where h is the height of the tree


def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)


def getLeftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left

    return currentNode


def getRightmostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent

    return currentNode.parent


'''-----------------------------------------------'''

# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# O(n) time | O(n) space - where n is the number of nodes in the tree


def findSuccessor(tree, node):
    inOrderTraversalOrder = getInOrderTraversalOrder(tree)

    for idx, currentNode in enumerate(inOrderTraversalOrder):
        if currentNode != node:
            continue

        # so we don't get index out of range and if we do find the matching node
        # we are not trying to get the next node if the matching node is at the
        # end of the array
        if idx == len(inOrderTraversalOrder) - 1:
            return None

        return inOrderTraversalOrder[idx + 1]


def getInOrderTraversalOrder(node, order=[]):
    if node is None:
        return order

    # left
    getInOrderTraversalOrder(node.left, order)
    # visit
    order.append(node)
    # right
    getInOrderTraversalOrder(node.right, order)

    return order

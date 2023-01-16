# Average: O(log(n)) time due to getting rid one of two sides of tree
#          O(log(n)) space

# Worst: O(n) time if there is a tree with only 1 side with values | O(1n space

def findClosestValueInBst(tree, target):
    # recursive function
    return findClosestValueInBestHelper(tree, target, tree.value)


def findClosestValueInBestHelper(tree, target, closest):
    if tree is None:
        return closest
    # if target value is farther away than tree value then updaed closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    # if target is less than tree value then look on left side of tree
    if target < tree.value:
        return findClosestValueInBestHelper(tree.left, target, closest)
    # if target is greater than tree value then look on right side of tree
    elif target > tree.value:
        return findClosestValueInBestHelper(tree.right, target, closest)
    # otherwise this means that target is equal to value so return closest
    else:
        return closest

# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


########## Second Solution ##########

# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

def findClosestValueInBst(tree, target):
    return findClosestValueInBestHelper(tree, target, tree.value)


def findClosestValueInBestHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Same solution as second solution but with explanation/break down
# Average: O(log(n)) time since we are technically removing either the entire left or
# right side of the tree when we go down a branch | O(1) space

# Worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
    # use currentNode var to track current tree for each recursive call
    currentNode = tree
    # iterate through tree as a long as the currentNode has children
    # this explores the entire branch getting closer to the target value till we reach None
    while currentNode is not None:
        # check if currentNode is closer than stored closest. If so, update closest
        # to current node's value
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        # make use of the BST property to determine what side of any given node has
        # values close to the target value and is therefore worth exploring
        # check if target is less than currentNode value. If so update currentNode to
        # the left node in the branch since this value will be smaller than the value to
        # the right therefore being possible closer to the target value
        if target < currentNode.value:
            currentNode = currentNode.left
        # check if target is greater than curretNode value. If so update currentNode to
        # the right node in the branch since this value will be greater than the value to
        # the left therefore being possibly closer to the target value
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

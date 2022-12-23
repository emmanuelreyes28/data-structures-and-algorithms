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

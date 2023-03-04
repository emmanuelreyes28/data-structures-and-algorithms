class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        # store bst object as currentNode
        currentNode = self

        while True:
            # values less than currentNode go to the left
            if value < currentNode.value:
                # make sure left node is emtpy, if so assign it this new value
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break  # break out of inifinite loop
                # otherwise loop through process again until we find a left node that
                # is empty so we can assign it the value
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        # srtore bst object as currentNode
        currentNode = self

        # keep iterating down the tree up until you reach a leaf node
        # if None is reached then value does not exist in tree therefore we return False
        # otherwise return true
        while currentNode is not None:
            # if value is less the the currentNode value then search on the left side of tree
            if value < currentNode.value:
                currentNode = currentNode.left
            # if value is greater than the currentNode value then search on the right side of tree
            elif value > currentNode.value:
                currentNode = currentNode.right
            # enter default case if value is equal to currentNode value meaning it is contained in the tree
            else:
                return True
        return False

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # this is a single-node tree; do nothing
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

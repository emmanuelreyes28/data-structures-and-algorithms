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

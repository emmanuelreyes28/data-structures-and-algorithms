# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space - where n is the number of nodes in the Linked List


def removeDuplicatesFromLinkedList(linkedList):
    # traverse through the linked list and check if the next value is the same as
    # the current value and not the end of ll. If so, repeatedly check the following node values
    # Once we reach a distict value point the currentNode to the new distinct node which
    # will remove duplicate node values

    # Once we reach None we know have reached the end of the linked list and we can
    # return the new linked list

    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode

    return linkedList

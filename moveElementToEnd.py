# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # create pointers at the beginning and end of array to be able to swap elements if necessary
    leftPointer = 0
    rightPointer = len(array) - 1
    # iterate through array as long as the pointer have not passed each other
    while leftPointer < rightPointer:
        # if the element is the same as toMove value then it is already in place since we are at the end
        # and we can decrement the right pointer by 1 (move inwards)
        if array[rightPointer] == toMove:
            rightPointer -= 1
        # if the element is NOT the same as toMove value then increment leftPointer by 1 since this value
        # should be in that same position
        elif array[leftPointer] != toMove:
            leftPointer += 1
        # if none of the pointers move this means we have to swap their values since the value at the
        # rightPointer needs to be in the position of the leftPointer and vice versa
        else:
            array[rightPointer], array[leftPointer] = array[leftPointer], array[rightPointer]
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))

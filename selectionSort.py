# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):
    # start position of our unsorted arrray
    currentIndex = 0
    # only going up to second to last element bc once we reach the last element
    # it will already be in the correct place (position)
    while currentIndex < len(array) - 1:
        smallestIndex = currentIndex
        # iterate throug remainder of unsorted array
        for i in range(currentIndex + 1, len(array)):
            # check for any smaller values and update accordingly
            if array[smallestIndex] > array[i]:
                smallestIndex = i
        # swap positions to put values in respective position
        array[currentIndex], array[smallestIndex] = array[smallestIndex], array[currentIndex]
        # increment currentIndex by 1 which reduces unsorted array len by 1
        currentIndex += 1
    return array

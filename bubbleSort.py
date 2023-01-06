# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        # loop through second to last value in array
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # swap values
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
    return array

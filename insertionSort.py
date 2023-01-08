# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i  # j is used to track the current number and its precendent value
        # for every swap made check if the swapped current number is less than the one before it
        # if so swap values and subtract j by 1 (going backwards on the list). Otherwise,
        # go to next number in the for loop.
        while j > 0 and array[j] < array[j-1]:
            # swap values
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


print(insertionSort([8, 5, 2, 9, 5, 6, 3]))

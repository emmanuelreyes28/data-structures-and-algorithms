# O(log(n)) time - since we reduce the values we have to search for by half on each iteration
# O(1) space
def binarySearch(array, target):
    # use left and right pointer to help determine the "range" of the array we
    # are searching through since we will be cutting our array by half on each iteration
    left = 0
    right = len(array) - 1
    # iterate through array as long as left pointer has not passed the right pointer
    # if this condition is not met it means that our target does not exist in array
    while left <= right:
        # middle is used as the midpoint of values being searched through. We round down middle using // 2
        middle = (left + right) // 2
        # store potentialMatch value using middle index position
        potentialMatch = array[middle]
        # if target matches potentialMatch then return the index position where it was found (middle)
        if target == potentialMatch:
            return middle
        # if target is less than potentialMatch then shift right pointer to the left by 1
        elif target < potentialMatch:
            right = middle - 1
        # otherwise shift left pointer to the right by 1. Shifting left and right pointers reduces the number
        # of values we have to search through
        else:
            left = middle + 1
    return -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))

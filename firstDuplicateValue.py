# O(n) time | O(1) space - where n is the length of the input array
# iterate through array if we have not yet come across the value turn it into a negative
# value. Once we come across a negative value we know we have visited this value before
# therefore it is a duplicate. We are able to do this because the given array is between
# 1 and n, inclusive, where n is the length of the array.
def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1


print(firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]))

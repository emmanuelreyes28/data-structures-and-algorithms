# O(n) time | O(n) space - where n is the lenght of the input array
def sortedSquaredArray(array):
    # create array stored with 0s that match the length of the array
    # this 0s position will be updated to store sorted squares
    sortedSquares = [0 for _ in array]

    # create pointers at the beginning and at the end for the given array
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    # traverse backwards on array to put the largest value at the end of sortedSquares
    # and work back as the values decrease reaching the beginning of the sortedSquares array
    # which will contain the smallest value
    for index in reversed(range(len(array))):
        # these values will be used to determine which is bigger using its absolute value
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        # we compare absolute values because when a value is squared even if negative its result
        # will still be positive

        # if smaller absolute value is larger than large absolute value then
        # store its squared value at the end of the sortedSquares array and increment
        # smallerValueIndex by 1 to shift over to the next value in the given array.
        # Otherwise do the same for largerValue but decrement index by 1 to shift to the
        # left (next value)
        if abs(smallerValue) > abs(largerValue):
            sortedSquares[index] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[index] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSquares

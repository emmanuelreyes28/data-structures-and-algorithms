# O(n) time | O(1) space - where n is the length of the input array
def longestPeak(array):
    # keep track of longest peak
    longestPeakLength = 0
    # index will start at 1 since a peak needs to have values to its left and right
    i = 1
    # iterate through the length of array - 1 since we will be looking forward 1 value
    while i < len(array) - 1:
        # determine if the current element is a peak considereing that the values to the left and right are decreasing
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        # if its not a peak keep iterating through array
        if not isPeak:
            i += 1
            continue

        # when we come across a peak look at the values to the left and right but looking 2 values back and forward
        # respectively since we have already accounted for the immediate values to the left and right. Keep incrementing
        # or decrementing respective to the direction until we come across a values that is not decreasing
        leftIndex = i - 2
        while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
            leftIndex -= 1
        rightIndex = i + 2
        while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
            rightIndex += 1
        # take the difference of indexes and subtract 1 to get the peak length.
        currentPeakLength = rightIndex - leftIndex - 1
        # update longestPeakLength using max function to determin which var is greater of the two
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        # assign index to rightIndex bc we have already considered all the items to the left.
        i = rightIndex
    return longestPeakLength


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))

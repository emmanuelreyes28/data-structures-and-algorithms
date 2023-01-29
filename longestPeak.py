def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIndex = i - 2
        while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
            leftIndex -= 1
        rightIndex = i + 2
        while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
            rightIndex += 1
        currentPeakLength = rightIndex - leftIndex - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIndex
    return longestPeakLength

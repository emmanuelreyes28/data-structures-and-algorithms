# O(n) time | O(1) space - where n is the length of the input array
def missingNumbers(nums):
    # store the expected totat for all nums in array inclusing 2 missin nums
    total = sum(range(1, len(nums) + 3))  # add 3 so the range is inclusive

    # substract the current nums from arr to calculate avg missing value
    for num in nums:
        total -= num
    averageMissingValue = total // 2

    # split nums arr in halves to find missing nums in upper and lower sides
    foundFirstHalf = 0
    foundSecondHalf = 0
    for num in nums:
        # the avg missing val will be a part of the first half of the arr
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    expectedFirstHalf = sum(range(1, averageMissingValue + 1))
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))

    # find the difference of both halves to get missing nums
    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]


print(missingNumbers([1, 4, 3]))

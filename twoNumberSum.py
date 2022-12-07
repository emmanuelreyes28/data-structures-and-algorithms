# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    # loop up until second to last value in the array
    for i in range(len(array) - 1):
        firstNum = array[i]
        #skip the current num so we do not add it to itself and go to the end of array
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    #if no hits return empty array
    return []

# O(n) time | O(n) space


def twoNumberSum(array, targetSum):
    #use hash table
    nums = {}

    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        #otherwise store current num in hash table
        else:
            nums[num] = True
    #if no hits return empty array
    return []

# O(nlog(n)) time | O(1) space


def twoNumberSum(array, targetSum):
    #sort array
    array.sort()

    #create left and right pointers
    left = 0
    right = len(array) - 1

    #check if left pointer has not passed the right one
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

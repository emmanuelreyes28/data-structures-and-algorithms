# O(n^2) time | O(n) space
# The nested loops in the solution run in O(n^2) time; this dwargs the O(nlog(n))
# runtime of the sorting step and allows us to remove it from the final time complexity
# of the algorithm.
def threeNumberSum(array, targetSum):
    # sort array of numbers to help algorith use left and right pointers
    # when searching for target sum
    array.sort()

    # create an empty array to store numbers that sum up to target sum
    triplets = []

    # iterate through array and subtract 2 from length bc we want to have 2
    # ending numbers left over to find the three numbers that sum up to target sum
    for i in range(len(array) - 2):
        # create left pointer starting to the right of the first value of the array
        left = i + 1
        # create right pointer starting at the end of the array
        right = len(array) - 1
        # continue iterating as long as our pointer have not overlapped or past each other
        while left < right:
            # store the current sum of all 3 numbers and check if is equal to targetSum
            # if so, append this array of numbers to triplets array and move both left and right
            # pointer by 1 respectively. This is done because if we only move the left pointer to the
            # right we are guaranteed that we will get a sum that is greater than our target and if we only
            # move the right pointer to the left then we are guaranteed that our sum will be less than our
            # target.
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            # if currentSum is less than target then we need to increase our sum by moving our left pointer
            # by 1 to the right. It is guaranteed that are sum will increase bc the array is sorted in
            # ascending order
            elif currentSum < targetSum:
                left += 1
            # if currentSum is greater than target then we need to decrease our sum by moving our right pointer
            # to the left by 1. It is guaranteed that are sum will decrease bc the array is sorted in
            # ascending order
            elif currentSum > targetSum:
                right -= 1
    return triplets


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))

# O(n) time | O(n) space - where n is the length of nums
def zeroSumSubarray(nums):
    # intialize set with 0 to check if it exists when we check num in nums
    sums = set([0])  # use a set for fast lookup

    # keep track of on going sum as we iterate trough nums
    currentSum = 0

    for num in nums:
        # add current num to currentSum
        currentSum += num
        # if we come across a currentSum that is already in the set then
        # we know that there is a subarray that equals to 0
        if currentSum in sums:
            return True
        # add currentSum to sum set
        sums.add(currentSum)

    # if we reach the end of the array then return False
    return False

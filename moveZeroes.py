# O(n) time | O(1) space
nums = [0, 1, 0, 3, 12]

slow = 0
for fast in range(len(nums)):
    if nums[fast] != 0 and nums[slow] == 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]

    # wait while we find a non-zero element to
    # swap with you
    if nums[slow] != 0:
        slow += 1

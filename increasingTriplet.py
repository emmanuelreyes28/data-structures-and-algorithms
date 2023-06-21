# O(1) space | O(n) time
def increasingTriplet(nums) -> bool:
    '''
        what is the question asking?
        - find three subsequent indices that increase in value from left to right
        - if such such indides and values exists return true otherwise return false
        '''
    f = float('inf')
    s = float('inf')

    for n in nums:
        # If n is less than f, it means n can be a potential candidate for the first element of an increasing triplet subsequence. So, it updates f to n.
        if n <= f:
            f = n
        # If n is greater than f and less than s, it means n can be a potential candidate for the second element of an increasing triplet subsequence. So, it updates s to n.
        elif n <= s:
            s = n
        # If n is greater than both f and s, it indicates the presence of an increasing triplet subsequence. So, it returns True.
        elif n > s:
            return True
    return False


print(increasingTriplet([20, 100, 10, 12, 5, 13]))

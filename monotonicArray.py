# O(n) time | O(1) space - where n is the length of the array
def isMonotonic(array):
    '''
    Iterate through array and check if previous value is either less than or greater than
    the currentValue. If it's less than then it must follow this pattern for every iteration
    making this array non-increasing (values only get smaller). If at any point during the 
    array the prevValue is greater than the currentValue when the array is supposed to be 
    non-increasing then this will make the isNonIncreasing value False. When we are done iterating
    both isNonDecreasing and isNonIncreasing will be false. In the return statement an or operator
    is used which means at least one of the varaibles must be True for the array to considered
    monotonic otherwise it will return False. 

    Vice versa if the array is considered to be non-decreasing.
    '''
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing


print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))

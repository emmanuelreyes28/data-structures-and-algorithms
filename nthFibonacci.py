# O(n) time | O(1) space
def getNthFib(n):
    # start with an array given the first two numbers of the fib sequence
    lastTwo = [0, 1]
    # counter starts at 3 since we have stored the first two values in the array above
    counter = 3
    # loop through the sequence and update the values in the lastTwo array respectively
    while counter <= n:
        # next fib num is the sum of the prev 2 nums
        nextFib = lastTwo[0] + lastTwo[1]
        # throw away the current value at index 0 and update with the value at index 1 in lastTwo array
        lastTwo[0] = lastTwo[1]
        # update the value at index 1 with the new nextFib num in the lastTwo array
        lastTwo[1] = nextFib
        # increment counter by 1 to reach n
        counter += 1
    # return value at index 1 if n > 1 otherwise return value at index 0
    # else statement covers if n = 0
    return lastTwo[1] if n > 1 else lastTwo[0]


# O(n) time | O(n) space
def getNthFib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]


print(getNthFib(6))

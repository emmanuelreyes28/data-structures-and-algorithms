# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # sort both arrays in place
    arrayOne.sort()
    arrayTwo.sort()

    # create pointers for arrays
    indexOne = 0
    indexTwo = 0

    # create vartiables to store and track smallest, current and smallest pairs for every iteration
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    # iterate through both arrays as long as you are still within range of both array lengths
    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        # store the current values from each array respectively
        firstNum = arrayOne[indexOne]
        secondNum = arrayTwo[indexTwo]
        # if the firstNum is less than secondNum store its current difference and
        # increment indexOne by 1 to get a closer (smaller) difference since the array is sorted
        if firstNum < secondNum:
            current = secondNum - firstNum
            indexOne += 1
        # if the secondNum is less than firstNum store its current difference and
        # increment indexTwo by 1 to get a closer (smaller) difference since array is sorted
        elif secondNum < firstNum:
            current = firstNum - secondNum
            indexTwo += 1
        # otherwise this mean both nums are equal meaning there diff is 0.
        # return these two values in an array
        else:
            return [firstNum, secondNum]
        # check if current is smaller than smallest, if so update smallest to be current (new smallest num)
        # and store this two nums and the smallestPair
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# O(n) time | O(1) space - although we do create an array to hold the threeLargest
# numbers it is a small length fixed array that its considered constant space
def findThreeLargestNumbers(array):
    # create array that holds 3 positions for the three largest numbers
    threeLargest = [None, None, None]
    # iterate through array to get each number and check if its largest than
    # any of the threeLargest numbers in respective array
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

# checks if the current numbers is larger than any of the already 3 existing
# numbers in the threeLargest number array. If so, update threeLargest array
# by shifting values inside


def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        # pass the index as an arg that you want the num to take place of
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

# iterates through the range of the given index to shift values over to the left


def shiftAndUpdate(array, num, index):
    # add 1 to index because range is exclusive
    for i in range(index + 1):
        # once we reach the desired index that was passed in the arg then update
        # its value to num
        if i == index:
            array[i] = num
        # else statement shifts values over to the left. In essence, it updates
        # the current index position value to the value that is to its right. It
        # iteratively does this till we hit the end of the loop
        else:
            array[i] = array[i + 1]


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))

# O(n) time | O(n) space - where n is the total number of elements in the array
def spiralTraverse(array):
    # store values as we spiral through nested array in result array
    result = []
    # create pointer to keep track of where we are in the array as we iterate (spiral) through
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    # keep iterating through arrays until we have reached the center (last value)
    # during the first iteration we are spiraling through the perimiter and then working our way in
    # by incrementing or decrementing startRow, endRow, startCol and endCol appropriately
    while startRow <= endRow and startCol <= endCol:
        # adds all values from left to right in first nested array to result array
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # adds all values at the end of each array using the end col index and iterating through the
        # remaining arrays we have. We add 1 to start row and end row so we do not add values that
        # already been added to result array and lets work inwards on our spiral.
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # add all values from the last nested array in reverse order. Use end row to get to last row
        # and count backwards (reverse) with col therefore adding the values in reverse order to result array
        for col in reversed(range(startCol, endCol)):
            # handle the edge case when theres a single row in the middle of the matrix. In this case,
            # we don't want to double count the values in this row, which we've already counted in the
            # first for loop above. See test case 2 below.
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # add all values from the first col not including the first and last values that have already
        # been added to the result array
        for row in reversed(range(startRow + 1, endRow)):
            # handle the edge case when there's a single column in the middlke of the matrix. In this case,
            # we don't want to double-count the values in this column, which we've already counted in the
            # second for loop above. See test case 3 below.
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        # update variables to spiral inwards
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result


# test case 1
print(spiralTraverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]))

# test case 2
print(spiralTraverse([
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]))

# test case 3
print(spiralTraverse([
    [1, 2, 3],
    [12, 13, 4],
    [11, 14, 5],
    [10, 15, 6],
    [9, 8, 7]
]))

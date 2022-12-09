#O(n) time | O(1) space - where is the length of the array
def isValidSubsequence(array, sequence):
    arrIndex = 0
    seqIndex = 0

    #loop through as long as indexes are less than lenght of respecitve arrays
    while arrIndex < len(array) and seqIndex < len(sequence):
        #check if current value is equal to each other if so move on to next value in seq array
        if array[arrIndex] == sequence[seqIndex]:
            seqIndex += 1
        #otherwise move onto next value in main array
        arrIndex += 1
    #once the loop exits, check if seqIndex is the same lenght as seq array meaning it covered
    #all values in seq array
    return seqIndex == len(sequence)

# O(n) time | O(1) space


def isValidSubsequence(array, sequence):
    seqIndex = 0

    #loop through main array
    for value in array:
        #check if the seqIndex is the same length as seq array then break out of loop
        if seqIndex == len(sequence):
            break
        #check if current sequence value is equal to curren main array value
        #if so then move onto next value in seq array
        if sequence[seqIndex] == value:
            seqIndex += 1
    #return boolean to check if all values in seq array were covered
    return seqIndex == len(sequence)

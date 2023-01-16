# #O(n) time | O(1) space - where is the length of the array
# def isValidSubsequence(array, sequence):
#     arrIndex = 0
#     seqIndex = 0

#     #loop through as long as indexes are less than lenght of respecitve arrays
#     while arrIndex < len(array) and seqIndex < len(sequence):
#         #check if current value is equal to each other if so move on to next value in seq array
#         if array[arrIndex] == sequence[seqIndex]:
#             seqIndex += 1
#         #otherwise move onto next value in main array
#         arrIndex += 1
#     #once the loop exits, check if seqIndex is the same lenght as seq array meaning it covered
#     #all values in seq array
#     return seqIndex == len(sequence)


'''
We only increment seqIndex by 1 if it matches the current value in the array.
In essence we wait till find a match for the first value in the given sequence with the value
in the array since the numbers aren't necessarily adjacent in the array but are in the 
same order as they appear in the array. 

It is possible for the array to continue iterating through the array even though we 
have already satisified the subsequence which we need to break out of the loop.
Here we check if the index value is the same length as the sequence meaning we have
found all values in the sequence within the array.

Lastly, if we reach the end of the array and all the values within the given sequence 
was not found then the condition will return False.
'''

# O(n) time | O(1) space


def isValidSubsequence(array, sequence):
    seqIndex = 0

    # loop through main array
    for value in array:
        # check if the seqIndex is the same length as seq array then break out of loop
        if seqIndex == len(sequence):
            break
        # check if current sequence value is equal to curren main array value
        # if so then move onto next value in seq array
        if sequence[seqIndex] == value:
            seqIndex += 1
    # return boolean to check if all values in seq array were covered
    return seqIndex == len(sequence)


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

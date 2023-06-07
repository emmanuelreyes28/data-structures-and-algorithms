class Solution:
    # O(n) time | O(n) space
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        need to traverse through both words and alternate the lettering
        if one word is longer than the other than append the remaining chars to the newString

        This iterator falls under the category of Terminating Iterators. It prints the values of       
        iterables alternatively in sequence. If one of the iterables is printed fully, the remaining 
        values are filled by the values assigned to fillvalue parameter.
        '''
        # return ''.join((a+b for a,b in zip_longest(word1, word2, fillvalue='')))

        # find smallest word
        smallest = min(len(word1), len(word2))
        # create new string to store and return result
        newString = ""

        # iterate through the smallest range and add chars to newString in alterate order
        for index in range(smallest):
            newString += word1[index]
            newString += word2[index]

        # find which word is larger and add the remaining chars to newString
        if len(word1) > len(word2):
            newString += word1[smallest:]
        else:
            newString += word2[smallest:]

        return newString

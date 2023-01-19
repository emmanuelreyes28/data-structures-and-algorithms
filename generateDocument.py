# O(n + m) time | O(c) space - where n is the number of characters, m is
# the length of the document, and c is the number of unique characters in the characters string
def generateDocument(characters, document):
    # count the frequency of characters in character string
    # compare that to what is in document string
    characterCounts = {}

    # counting frequency of character in characters
    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1

    # loop through document and check if character exists in hashmap
    # if does NOT or its value is 0 (meaning we did not have enough of said character) return False
    # otherwise decrement its value by 1
    # if we are able to exit the for loop successfully return true
    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1

    return True

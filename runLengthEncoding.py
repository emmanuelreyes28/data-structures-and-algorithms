# O(n) time | O(n) space - where n is the length of the input string
def runLengthEncoding(string):
    # the input string is guaranteed to be non-empty,
    # so our first run will be of at least length 1
    encodedStringCharacters = []
    currentRunLength = 1

    # start iterating from index 1 and check if current value is same as prev value
    for i in range(1, len(string)):
        currentChar = string[i]
        prevChar = string[i - 1]

        # if char not the same or max length reach add encoded to list
        if currentChar != prevChar or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(prevChar)
            currentRunLength = 0

        currentRunLength += 1

    # handle the last run
    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])

    return "".join(encodedStringCharacters)

# O(n * m) time | O(c) space - where n is the number of strings, m is the
# length of the longest string, and c is the number of unique characters across
# all strings
def commonCharacters(strings):
    characterCounts = {}
    for string in strings:
        uniqueStringChars = set(string)
        for char in uniqueStringChars:
            if char not in characterCounts:
                characterCounts[char] = 0
            characterCounts[char] += 1

    finalCharacters = []
    for character, count in characterCounts.items():
        if count == len(strings):
            finalCharacters.append(character)

    return finalCharacters

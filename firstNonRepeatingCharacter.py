# O(n) time | O(1) space - where n is the length of the input string
# the constant space is because the input string only has lowercase
# english-alphabet letters; thus, our hash table will never have more
# than 26 character frequencies
def firstNonRepeatingCharacter(string):
    # use map to track frequency of each character in string
    characterFrequencies = {}

    # iterate through string and add each character to map
    for character in string:
        # .get(character, 0) adds the char if it does not exist and assigns it a value of 0
        # value then gets 1 added to it
        characterFrequencies[character] = characterFrequencies.get(
            character, 0) + 1

    # iterate through string and find the first character that has a value
    # of 1 in the map. Return its index position.
    for index in range(len(string)):
        character = string[index]
        if characterFrequencies[character] == 1:
            return index

    # return -1 meaning no character in map had a value of 1 (unique)
    return -1

# # O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
    # important to use mod for newKey in case key is larger than 26
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)


def getNewLetter(letter, key):
    # get new unicode
    newLetterCode = ord(letter) + key
    if newLetterCode <= 122:
        # return unicode to character
        return chr(newLetterCode)
    else:
        # return unicode character using mod to get remainder
        return chr(96 + newLetterCode % 122)


print(caesarCipherEncryptor("xyz", 27))

### Solution without using unicode ###

# O(n) time | O(n) space


def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)


def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode % 26]


print(caesarCipherEncryptor("xyz", 5))

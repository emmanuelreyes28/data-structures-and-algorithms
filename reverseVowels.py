# O(n) time | O(n) space
def reverseVowels(s: str) -> str:
    '''
    since vowels can show in upper or lower case we should make the string lowercase
    we are basically swapping each vowels place as we iterate through the string
    use a left pointer and right pointer
    check if either pointer is a vowel (can use set for O(1) lookup time)
    if so swap it with the other pointer position if its also a vowel or until it comes across a
    vowel.
    keep iterating as long as left point is less than right pointer
    '''
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    reversedString = list(s)

    leftPointer = 0
    rightPointer = len(s) - 1

    while leftPointer < rightPointer:
        if reversedString[leftPointer] in vowels and reversedString[rightPointer] in vowels:
            reversedString[leftPointer], reversedString[rightPointer] = reversedString[rightPointer], reversedString[leftPointer]
            leftPointer += 1
            rightPointer -= 1
        elif reversedString[leftPointer] not in vowels:
            leftPointer += 1
        elif reversedString[rightPointer] not in vowels:
            rightPointer -= 1
    return "".join(reversedString)

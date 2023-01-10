# O(n) time | O(1) space
def isPalindrome(string):
    # check len of string is 1 then return true
    if len(string) == 1:
        return True

    # check if char are the same on both ends working in using pointers
    first_index = 0
    last_index = len(string) - 1

    while first_index < last_index:
        first_pointer = string[first_index]
        second_pointer = string[last_index]

        if first_pointer == second_pointer:
            first_index += 1
            last_index -= 1
        else:
            return False

    return True

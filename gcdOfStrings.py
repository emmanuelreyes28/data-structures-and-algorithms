def gcdOfStrings(str1: str, str2: str) -> str:
    '''
    Time Complexity: min(m,n) * (n + m)
    '''

    len1, len2 = len(str1), len(str2)

    def isDivisor(l):
        # check if the lengths of str1 and str2 are divisible by current lenght (l) with no remainder
        if len1 % l or len2 % l:
            return False
        # find the factors of str1 and str2 by divinding their lengths by current length(l)
        f1, f2 = len1 // l, len2 // l
        # check if the given substring times their factors are equal to their original string, if so then we have found our gcd
        return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

    # using a greedy approach take the smallest string and check if it divides both str1 and str2
    # otherwise keep shortening the string by 1 char
    for l in range(min(len1, len2), 0, -1):
        if isDivisor(l):
            return str1[:l]
    return ""


print(gcdOfStrings("ABABAB", "ABAB"))

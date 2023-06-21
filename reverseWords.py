# O(n) space | O(n) time
def reverseWords(self, s: str) -> str:
    '''
    what is the problem asking?
    - given string s which is a phrase return the string (phrase) in reverse order
    - must remove spaces in beginning and end of string
    - must only have one space seperating each word

    can split given string into a list and reverse the list and then joing the strings with a
    space in between 
    '''

    reverse = [word for word in s.split(' ') if word != '']
    return ' '.join(reverse[::-1])

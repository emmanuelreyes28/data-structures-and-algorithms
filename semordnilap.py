# O(n * m) time | O(n * m) space - where n is the number of words and m is
# the length of the longest word
def semordnilap(words):
    # create set of words which removes any duplicates and allows for fast lookups
    # since sets are implemented using hash tables
    wordsSet = set(words)
    # creaste an empty array to store pairs
    semordnilapPairs = []

    # iterate through list of words and reverse each one.
    for word in words:
        reversed = word[::-1]
        # check if the reversed word exist in set and is not the same word
        if reversed in wordsSet and reversed != word:
            # add pair to list of pairs
            semordnilapPairs.append([word, reversed])
            # remove word and reversed word from set so it doesnt cause pair duplicates
            # as we iterate through the remaining list
            wordsSet.remove(word)
            wordsSet.remove(reversed)
    return semordnilapPairs


print(semordnilap(["dog", "hello", "desserts", "test", "god", "stressed"]))

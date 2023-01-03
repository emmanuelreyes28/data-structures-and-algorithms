# O(n log(n)) time | O(1) space - where n is the number of tandem bicycles
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    '''
    If fastest is true then we want to find the maximum total speed. Which can be done by
    sorting both arrays and pairing the last value in first arrray and first value in the
    second array. Here we are pairing the highest value from one array with the lowest value
    from the other array.

    If fastest is false then we want to find the minimum total speed. Which can be done by
    reversing one of the two arrays after it has been sorted to then pair the last value in 
    first arrray and first value in the second array. In essence we are pairing the highest
    values together.
    '''

    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    totalSpeed = 0

    for index in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[index]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - index - 1]
        totalSpeed += max(rider1, rider2)

    return totalSpeed


def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        # swap values
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

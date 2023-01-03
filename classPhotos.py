# O(nlog(n)) time | O(1) space - where n is the number of students
def classPhotos(redShirtHeights, blueShirtHeights):
    '''
    First thought is to sort both of the arrays in descending order. Since student with the 
    same colored shirt have to be in the same row we need to strictly have one of the two 
    arrays have larger numbers (heights) than the other. If this is possible, return True. 
    Otherwise, return False.
    '''
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFirstRow = "blue"

    if redShirtHeights[0] < blueShirtHeights[0]:
        shirtColorInFirstRow = "red"

    for index in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[index]
        blueShirtHeight = blueShirtHeights[index]

        if shirtColorInFirstRow == "red":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    return True

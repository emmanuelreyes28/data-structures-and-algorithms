#O(n) time where n is the total number of elements in the array, including sub-elements
#O(d) space where d is the greatest depth of special arrays in the array
def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            #make recursive call
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

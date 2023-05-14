# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
    # create determined length arrays with value 1 as placeholder
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    # get the product of all values to the left of element
    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    # get the product of all values to the right of element
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    # populate products array with result by multiplying the values at the
    # given index
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products


print(arrayOfProducts([1, 2, 3, 4]))

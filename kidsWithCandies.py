# O(n) time | O(n) space
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    '''
        1. Find the largest num in the array
        2. iterate through each ith kid and add the given extra candies to their candies
        3. check if the currentSum is greater than or equal to the largest num in the array
        4. if so, append True to the array
        5. else append False to the array
        '''

    # largest = max(candies)
    # result = []

    # for i in range(len(candies)):
    #     currentSum = extraCandies + candies[i]
    #     if currentSum >= largest:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result

    maxCandies = max(candies)
    result = [False for c in candies]
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandies:
            result[i] = True
    return result

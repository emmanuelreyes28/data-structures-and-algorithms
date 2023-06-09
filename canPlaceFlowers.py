def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    '''
    1. iterate through the flowerbed
    2. check if its a 0 and the num before it and after it are 0 then we can plant here
    3. reduce n by 1 (n-1)
    4. check if n == 0 return true else return false
    '''
    if n == 0:
        return True

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False

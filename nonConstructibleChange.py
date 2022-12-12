# O(nlogn) time | O(1) space - where n is the number of coins
# It takes O(nlogn) time to sort an array
def nonConstructibleChange(coins):
    #sort coins in ascending order
    coins.sort()

    #track current change that you can give back
    current_change = 0

    #iterate through coins
    for coin in coins:
        #check if current coin is larger than current change + 1
        #if so return current change + 1 because this change cannot be given
        if coin > current_change + 1:
            return current_change + 1
        #otherwise add current coin to current change
        current_change += coin
    #once exiting the loop return the current change + 1
    return current_change + 1

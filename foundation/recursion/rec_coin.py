# Python 3.7.2
# Given a target amount n and a list (array) of distinct coin values, 
# what's the fewest coins needed to make the change amount
# ex. if n = 10 and coins = [1,5,10]
# with 1 coin being the minimum amount


def rec_coin(target,coins):

    # Default to target value
    min_coins = target

    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1

    else:

        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins = 1 + rec_coin(target-i,coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:

                min_coins = num_coins  # reset minimum

    return min_coins


"""

Test
rec_coin(63,[1,5,10,25])

"""
# Python 3.7.2
# Level 2
# Given three integers between 1 and 11
# if the sum is less than or euqla to 21, return their sum
# if their sum exceeds 21 and there is an 11, reduce the total sum by 10
# finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21: # sum expect at most 2 arguments
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31: # case for 21 < sum < 31
        return sum([a,b,c]) - 10
    else:
        print('BUST')

if __name__ == "__main__":
    print(blackjack(5,6,11))

# key
# sum([a,b,c])
# 11 in [a,b,c]
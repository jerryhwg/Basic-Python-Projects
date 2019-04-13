# Python 3.7.2
# Level 3
# Take in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1

if __name__ == "__main__":
    print(spy_game([1,0,2,4,0,5,7]))

# key: code = [0,0,7,'x']
# key: code.pop(0)
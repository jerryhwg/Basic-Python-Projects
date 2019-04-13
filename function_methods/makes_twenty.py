# Python 3.7.2
# Level 0
# Given two integers
# Return True if the sum of the integer is 20 or if one of the integers is 20
# If not, return false

def makes_twenty(n1,n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20

if __name__ == "__main__":
    print(makes_twenty(5,15))

# key: return for True or False
# Python 3.7.2
# Level 0
# Returns the lesser of two given numbers if both numbers are even
# Returns the greater if one or both numbers are odd

def lesser_of_two_evens(n1,n2):
    if n1%2 == 0 and n2%2 == 0:
        return min(n1,n2)
    else:
        return max(n1,n2)

if __name__ == "__main__":
    print(lesser_of_two_evens(2,5))

# key: min(n1,n2), max(n1,n2)
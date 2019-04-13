# Python 3.7.2
# Level 1
# Integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return (abs(100-n) <= 10 or abs(200-n) <= 10)

if __name__ == "__main__":
    print(almost_there(107))

# key: abs(100-n)
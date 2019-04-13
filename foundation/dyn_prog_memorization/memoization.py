cache = {}

def memoizedAddTo80(n):
    if n in cache:
        return cache[n]
    else:
        print("long time")
        cache[n] = 5 + 80
        return cache[n]
    
print("1", memoizedAddTo80(5))
print("2", memoizedAddTo80(5))


'''
Result
long time
1 85
2 85
'''
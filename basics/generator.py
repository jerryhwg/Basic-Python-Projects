'''
Generators allow us to generate as we go along, instead of holding everything in memory.
Generators are best for calculating large sets of results 
(particularly in calculations that involve loops themselves) 
in cases where we don’t want to allocate the memory 
for all of the results at the same time.
'''

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a # only keep track of the previous result instead of holding every single result in memory
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)

'''
cf)

def gen_fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output
'''
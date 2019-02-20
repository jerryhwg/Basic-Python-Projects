mySentence = 'loves the color'

color_list = ['red','blue','green','pink','white','black']

def color_function(name):
    lst = [] # declar an empty local var (lst)
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst # return (lst) to the calling from main

# when calling a function, pass in the required arg (name)
lst = color_function('Jesse') # receive the returned (lst)

for i in lst:
    print(i)

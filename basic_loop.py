mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'pink', 'white', 'black']


def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst # return (lst) to the get_name()


def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '': # if name is empty
            print("You need to provide your name!")
        else:
            go = False # get the name and stop here
    # call color_function with the arg(nam) and receive the return(lst)
    lst = color_function(name) 

    for i in lst:
        print(i)


get_name() # main call

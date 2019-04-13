'''
Decorator
function which modify the functionality of another function
help your code shorter and more "Pythonic"
use @ symbol
useful for web development, such as Flask or Django
'''

def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function') # decorating

        original_func()

        print('Some extra code, after the original function') # decorating

    return wrap_func()


@new_decorator # to disable just add # in the head
def func_needs_decorator():
    print("I want to be decorated!!")


'''
Test:
func_needs_decoator()

Some extra code, after the original function
I want to be decorated!!
Some extra code, after the original function

'''
# Python 3.7.2
# Module 67
# Implementation of a Satack

class Stack(object):

    def __init__(self):
        self.items = [] # no item in the list yet

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1] # show the last added item

    def size(self):
        return len(self.items)



"""

Test

s = Stack()
s.isEmpty()
s.push(1)
s.push('two')
s.peek()
s.push(True)
s.size()
s.isEmpty()
s.pop()

"""
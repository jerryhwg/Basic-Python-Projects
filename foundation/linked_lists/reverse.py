# Python 3.7.2
# a function to reverse a linked list in pace
# take in the head of the list as input and return the new head of the list


def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:

        nextnode = current.nextnode
        current.nextnode = previous # order of the previous and this is important

        previous = current
        current = nextnode

    return previous

"""

class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

"""

"""

Test

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

reverse(a)
print (d.nextnode.value)
3
print (c.nextnode.value)
2
print (b.nextnode.value)
1
print (a.nextnode.value)
Error

"""
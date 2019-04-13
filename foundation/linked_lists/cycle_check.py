# Python 3.7.2
# Given a singly linked list, write a function which takes in the first node in the singly linked list
# and returns a boolean indicating if the linked list contains a "cycle"
# a node's next point points back to a previous node in the list instead of a new node


def cycle_check(node):

        # return a boolean if cycle
        marker1 = node
        marker2 = node
        
        while marker2 != None and marker2.nextnode != None:

            marker1 = marker1.nextnode
            marker2 = marker2.nextnode.nextnode # marker2 is at 2 nodes ahead

            if marker2 == marker1: # for any circle existence
                return True

        return False


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

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle!

x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z
# No cycle

"""
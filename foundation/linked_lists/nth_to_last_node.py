# Python 3.7.2
# a function that takes a head node and an integer value n
# and returns the nth to last node in the linked list
# a bunch of nodes
# a block = n-wide nodes ex. n=2, 2-wide nodes
# once the front of the block reaches the end, the other end of the block is the Nth node


def nth_to_last_node(n, head): # head = a

    left_pointer = head
    right_pointer = head

    # set right pointer
    for i in range(n-1):

        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.nextnode # set the block (left_pointer = head, right_pointer = right_pointer.nextnode)

    while right_pointer.nextnode: # continue to loop (slide the block) until 'right_pointer.nextnode' reaching the tail

        left_pointer = left_pointer.nextnode # ex. n =2, d
        right_pointer = right_pointer.nextnode # ex. e

    return left_pointer # when the end is e, the Nth pointer is d and d.value is 4



"""

class Node:

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
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = nth_to_lst_node(2, a)
# 2nd to last node = d with a value of 4
target_node.value
4

"""
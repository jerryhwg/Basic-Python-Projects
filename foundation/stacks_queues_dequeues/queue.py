# Python 3.7.2
# Module 69
# Implementation of Queue

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



"""

Test

q = Queue()
q.size()
q.isEmpty()
q.enqueue(1)
q.enqueue(2)
q.dequeue()

"""
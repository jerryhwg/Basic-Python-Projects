"""
Python 3.7.2

Implement a Queue class using two stacks
stack1=[]
stack2=[]

class Queue2Stacks(object)

Test
q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue(i))
"""

class Queue2Stacks(object):

    def __init__(self):

        self.instack = []
        self.outstack = []

    def enqueue(self,element):
        
        self.instack.append(element) # stack, append => instack list
        # ex. 12345

    def dequeue(self): # double reversal(pop())
        if not self.outstack: # check if outstack not exist
            while self.instack: # while instack exists
                self.outstack.append(self.instack.pop()) # outstack list, ex. 54321
        return self.outstack.pop() # ex. 12345 = dequeue (remove the front elemenet)
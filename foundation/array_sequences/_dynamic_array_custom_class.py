# Python 3.7.2
# A custom dynamic array like python list

import ctypes
# ctypes is a foreign function library for Python
# it provides C compatible data types, and allows calling functions in DLLs or shared libraries

class DynamicArray(object):
    
    def __init__(self): # initiate
        
        self.n = 0 # default 0 count
        self.capacity = 1 # default capacity 1
        self.A = self.make_array(self.capacity) # create array
        
    def __len__(self):
        return self.n # length of array
    
    def __getitem__(self,k):
        
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds!') # check if k index is in bounds of array
        
        return self.A[k] # retrieve from array at index k
    
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity) # double capacity if not enough room
            
        self.A[self.n] = ele # set self.n index to element
        self.n += 1
        
    def _resize(self,new_cap):
        
        B = self.make_array(new_cap) # new bigger array
        
        for k in range(self.n): # reference all existing values
            B[k] = self.A[k]
            
        self.A = B # call A the new bigger array
        self.capacity = new_cap # reset the capacity
        
    def make_array(self,new_cap):
        
        return (new_cap * ctypes.py_object)() # return a new array with new_app capacity
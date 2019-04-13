"""
activities sorted by finish time
maximum number of activities that can be taken by a single person,
assuming that a person can only work on a single activity at a time
"""

def printMaxActivities(s, f): 
    n = len(f) 
    print("The following activities are selected")
  
    # The first activity is always selected 
    i = 0
    print(i) 
  
    # Consider rest of the activities 
    for j in range(n):
  
        # If this activity has start time greater than 
        # or equal to the finish time of previously 
        # selected activity, then select it 
        if s[j] >= f[i]:
            print(j)
            i = j 
  
# Driver program to test above function 
s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
printMaxActivities(s, f) 

"""
first activity is always selected: index 0
finish time of the first activity is 2
the start time of next activity must be greater or equal to 2
s[1]=3 is valid: index 1
finish time of the second activity is 4
s[2]=0 is not valid
s[3]=5 is valid: index 3
finish time of the third activity is 7
s[4]=8 is greater than 7: index 4
so index 0, 1, 3, 4 is the valid activities
"""
# Python 3.7.2
# Level 3
# Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 
# and extending to the next 9 (every 6 will be followed by at least one 9)
# Return 0 for no numbers

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num # 2+1=3
                break # exit while loop -> go to for loop
            else:
                add = False # add = False then move to the next while loop
        while not add: # add = False
            if num != 9: # ignore till else (if num = 9)
                break # exit while loop -> for loop, but still add = False
            else: # if num = 9, exit the loop, go to for loop with add = True to resume (total += num)
                add = True # go to for loop, but add = True
    return total

if __name__ == "__main__":
    print(summer_69([2, 1, 6, 9, 11]))

# key: for loop with two while loop
# unordered list

def seq_search(arr, ele):

    pos = 0
    found = False

    while pos < len(arr) and not found: # not found == False

        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    return found


'''
arr = [1,2,3,4,5]
seq_search(arr,6)

False
'''
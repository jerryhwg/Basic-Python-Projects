# ordered/sorted list

def ordered_seq_search(arr,ele):

    '''
    Input array must be ordered/sorted
    '''

    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:

        if arr[pos] == ele:
            found = True

        else:
            if arr[pos] > ele: # key
                stopped = True

            else:
                pos += 1

    return found
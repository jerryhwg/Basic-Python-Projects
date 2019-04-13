# either positionOfMax or positionOfMin

def selection_sort(arr):

    for fillslot in range(len(arr)-1,0,-1): # 4 3 2 1

        positionOfMax = 0 

        for location in range(1,fillslot+1): # range(1,5): 1 2 3 4 

            if arr[location] > arr[positionOfMax]: # if arr[1] > arr[0]
                positionOfMax = location # positionOfMax = 1
        # repeat loop to confirm the positionOfMax

        # once the positionOfMax is confirmed in the first round of loop, swap arr[positionOfMax] with arr[4]
        # move to the right end
        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp

'''
arr = [5,8,3,10,1]
selection_sort(arr)
arr
'''
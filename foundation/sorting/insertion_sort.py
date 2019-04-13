def insertion_sort(arr):

    for i in range(1,len(arr)): # 1 2 3 4

        currentvalue = arr[i] # arr[1]
        position = i # 1

        while position > 0 and arr[position-1] > currentvalue: # arr[0] > arr[1]

            arr[position] = arr[position-1] # swap arr[0] moves to arr[1]; insert
            position = position-1 # position = 0

        arr[position] = currentvalue # arr[0] = currentvalue
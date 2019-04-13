def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        # 3 2 1
        print("This is the n: ",n)
        for k in range(n):
            # if n = 3, k = 0 1 2
            print("This is the k index check: ",k)
            if arr[k] > arr[k+1]:
                # arr[k] = 5, arr[k+1] = 3
                temp = arr[k] # temp = 5
                arr[k] = arr[k+1] # swap: arr[k] = 3
                arr[k+1] = temp # arr[k+1] = 5


'''
arr = [5,3,7,2]
bubble_sort(arr)
arr
'''
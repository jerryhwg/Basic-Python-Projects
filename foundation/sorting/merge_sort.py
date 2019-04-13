def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr)//2 # divide
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf) # recursion(tree)
        merge_sort(righthalf) # recursion(tree)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1

            else:
                arr[k] = righthalf[j] # swap
                j += 1

            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    print("Merging", arr)


'''
arr = [5,3,7,2,9,8,1,3]
merge_sort(arr)
arr
'''
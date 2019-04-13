# only work on ordered list

def rec_bin_search(arr,ele):

    # Edge case
    if len(arr) == 0:
        return False

    else:

        mid = len(arr)//2

        if arr[mid] == ele:
            return True

        else:

            if ele < arr[mid]:
                return rec_bin_search(arr[:mid],ele) # recurive search

            else:
                return rec_bin_search(arr[mid+1:],ele) # recursive search


'''
arr = [1,2,3,4,5,6,7,8,9,10]
rec_bin_search(arr,3)

for n in range(1,11):
    result = binary_search(arr,n)
    print(result)
'''

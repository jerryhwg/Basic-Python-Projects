# only work on ordered list

def binary_search(arr,ele):

    first = 0
    last = len(arr)-1

    found = False

    while first <= last and not found:

        mid = (first+last)//2

        if arr[mid] == ele:
            found = True # return found
        else:
            if ele < arr[mid]:
                last = mid - 1 # iterate until if arr[mid] == ele
            else:
                first = mid + 1 # iterate until if arr[mid] == ele

    return found # from if arr[mid] == ele


'''
arr = [1,2,3,4,5,6,7,8,9,10]
binary_search(arr,3)

for n in range(1,11):
    result = binary_search(arr,n)
    print(result)
'''
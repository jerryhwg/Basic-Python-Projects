# Python 3.7.2
# Level 1
# A list of integers
# Return True if the array contains a 3 right next to a 3 somewhere in the list

def has_33(nums):
    for i in range(0,len(nums)-1): # eg. if nums = 8, nums[0]~nums[7]
        if nums[i:i+2] == [3,3]: # eg. nums[1:3] = num[1]~num[2] == [3,3]
            return True
    return False

if __name__ == "__main__":
    print(has_33([1,3,3,7]))

# key: nums[i:i+2]
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0: # if the list is empty, return -1
        return -1 # not found

    middle_index = (start+end)//2 # start at middle index
    middle_value = arr[middle_index]

    if middle_value == target:  # if the middle_index is the target, return the middle_index
        return middle_index
    else:
        if middle_value < target:
            return binary_search(arr, target, middle_index, end)
        if middle_value > target:
            return binary_search(arr, target, start, middle_index)

    return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, -8, 0, len(arr1)-1))
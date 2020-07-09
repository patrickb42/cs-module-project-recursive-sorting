def binary_search(arr, target, start, end, asc=True):
    if start > end:
        return -1
    middle = (end - start) // 2 + start
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search(arr, target, start, middle - 1) if asc else binary_search(arr, target, middle + 1, end, False)
    else:
        return binary_search(arr, target, middle + 1, end) if asc else binary_search(arr, target, start, middle - 1, False)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    asc = True if arr[0] < arr[-1] else False
    return binary_search(arr, target, 0, len(arr), asc)

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print(f'arrA: {arrA}, arrB: {arrB}')
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a_index = 0
    b_index = 0
    merged_arr_index = 0

    def finish_appending(src, src_index, dst, dst_index):
        for _ in range(len(src) - src_index):
            dst[dst_index] = src[src_index]
            src_index += 1
            dst_index += 1

    while True:
        if a_index >= len(arrA):
            finish_appending(arrB, b_index, merged_arr, merged_arr_index)
            break
        elif b_index >= len(arrB):
            finish_appending(arrA, a_index, merged_arr, merged_arr_index)
            break

        if arrA[a_index] < arrB[b_index]:
            merged_arr[merged_arr_index] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[merged_arr_index] = arrB[b_index]
            b_index += 1

        merged_arr_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    left_half = arr[ : len(arr) // 2]
    right_half = arr[(len(arr) // 2): ]

    return merge(merge_sort(left_half), merge_sort(right_half))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

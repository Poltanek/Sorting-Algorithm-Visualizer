import time

def merge_sort(arr, drawData, timeTick, stop_check):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], drawData, timeTick, stop_check)
    right_half = merge_sort(arr[mid:], drawData, timeTick, stop_check)
    
    return merge(left_half, right_half, arr, drawData, timeTick, stop_check)

def merge(left, right, arr, drawData, timeTick, stop_check):
    result = []
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if stop_check():
            return arr
        if left[i] < right[j]:
            result.append(left[i])
            arr[k] = left[i]
            i += 1
        else:
            result.append(right[j])
            arr[k] = right[j]
            j += 1
        k += 1
        drawData(arr, ['green' if x == k else 'red' for x in range(len(arr))])
        drawData(arr, ['green' if x == k else 'red' for x in range(len(arr))])
    
    while i < len(left):
        if stop_check():
            return arr
        result.append(left[i])
        arr[k] = left[i]
        i += 1
        k += 1
        drawData(arr, ['green' if x == k else 'red' for x in range(len(arr))])
    
    while j < len(right):
        if stop_check():
            return arr
        result.append(right[j])
        arr[k] = right[j]
        j += 1
        k += 1
        drawData(arr, ['green' if x == k else 'red' for x in range(len(arr))])

    return arr

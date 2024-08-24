import time

def merge_sort(arr, drawData, timeTick):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], drawData, timeTick)
    right_half = merge_sort(arr[mid:], drawData, timeTick)
    
    return merge(left_half, right_half, arr, drawData, timeTick)

def merge(left, right, arr, drawData, timeTick):
    result = []
    i = j = k = 0
    
    while i < len(left) and j < len(right):
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
        time.sleep(timeTick)
    
    while i < len(left):
        result.append(left[i])
        arr[k] = left[i]
        i += 1
        k += 1
        drawData(arr, ['green' if x == k else 'red' for x in range(len(arr))])
        time.sleep(timeTick)

    while j < len(right):
        result.append(right[j])
        arr[k] = right[j]
        j += 1
        k += 1
        drawData(arr, ['green' if x == k else 'red' for x in range(len(arr))])
        time.sleep(timeTick)
    
    return result



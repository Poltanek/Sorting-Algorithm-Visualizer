import time

def heap_sort(data, drawData, speed, timeTick):
    n = len(data)
    time.sleep(timeTick)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, speed, timeTick)

    # Extract elements from heap one by one
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Swap
        heapify(data, i, 0, drawData, speed)
        drawData(data, ['green' if x == i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
def heapify(arr, n, i, drawData, speed, timeTick):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        drawData(arr, ['yellow' if x == i or x == largest else 'red' for x in range(len(arr))])
        time.sleep(timeTick)
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest, drawData, speed)

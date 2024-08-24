import time

# this method is used to sort the data using bubble sort algorithm
# data: list of integers to be sorted
# drawData: method to draw the data on the canvas
# timeTick: time delay between each iteration
# return: None

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
        drawData(data, ['green' for _ in range(len(data))])
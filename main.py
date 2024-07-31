from tkinter import * 
from tkinter import ttk 
import numpy as np 
import random 
import time 

mainWindow = Tk()
mainWindow.title("Sorting Algorithm Visualizer")
mainWindow.geometry("800x600")
mainWindow.config(bg="black")

# Variables
selected_alg = StringVar()
data = []

def drawData(data):
    MainCanvas.delete("all")
    a_height = 380
    a_width = 600
    x_width = a_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # Top Left
        x0 = i * x_width + offset + spacing
        y0 = a_height - height * 340
        # Bottom Right
        x1 = (i + 1) * x_width + offset
        y1 = a_height
        MainCanvas.create_rectangle(x0, y0, x1, y1, fill="red")
        MainCanvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    mainWindow.update_idletasks()

def GenerateArray():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(SizeEntry.get())
    
    if minVal < 0 : minVal = 0
    if maxVal > 100 : maxVal = 100
    if size > 30 or size < 3 : size = 25
    if minVal > maxVal : minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))
    
    drawData(data)

def bubble_sort(data):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            drawData(data)
            time.sleep(float(SpeedScale.get()))
    drawData(data)

def StartAlgorithm():
    global data
    selected_algorithm = selected_alg.get()
    if selected_algorithm == "Bubble Sort":
        bubble_sort(data)


# Frames & Canvas 
# Row 0 
UserInterface = Frame(mainWindow, bg="black")
UserInterface.grid(row=0, column=0, padx=15, pady=5)
MainCanvas = Canvas(mainWindow, bg="white", width=600, height=380)
MainCanvas.grid(row=2, column=0, padx=10, pady=5)

# Buttons & Labels & Entries

SelectLbl = Label(UserInterface, text="Select Algorithm", bg="black", fg="white")
SelectLbl.grid(row=0, column=0, padx=5, pady=5, sticky=W)
AlgMenu = ttk.Combobox(UserInterface, textvariable=selected_alg, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"], state="readonly")
AlgMenu.grid(row=0, column=1, padx=5, pady=5)
AlgMenu.current(0)

GenerateArrayBtn = Button(UserInterface, text="Generate Array", command=GenerateArray, bg="black", fg="white")
GenerateArrayBtn.grid(row=0, column=2, padx=5, pady=5)

SpeedScale = Scale(UserInterface, from_=0.1, to=2.0, bg="black", fg="white", length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
SpeedScale.grid(row=0, column=3, padx=5, pady=5)


# Row 1
SizeEntry = Scale(UserInterface, from_=3, to=30, bg="black", fg="white", length=200, resolution=1, orient=HORIZONTAL, label="Select Size")
SizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

minEntry = Scale(UserInterface, bg="black", fg="white", from_=0, to=10, length=200, resolution=1, orient=HORIZONTAL, label="Select Min Value")
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

maxEntry = Scale(UserInterface, bg="black", fg="white", from_=10, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Select Max Value")
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

startBtn = Button(UserInterface, command=bubble_sort, text="Start Sorting", bg="black", fg="white")
startBtn.grid(row=1, column=6, padx=5, pady=5)


mainWindow.mainloop()

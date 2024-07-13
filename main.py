from tkinter import *
from tkinter import ttk
import numpy as np
import random 

mainWindow = Tk()
mainWindow.title("Sorting Algorithm Visualizer")
mainWindow.geometry("800x600")
mainWindow.config(bg="black")

# Variables
selected_alg = StringVar()

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
        MainCanvas.create_text(x0 + 2, y0, anchor=SW, text=str(height))


def GenerateArray():
    print('Alg Selected: ' + selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 10
    try:
        size = int(SizeEntry.get())
    except:
        size = 10
    
    if minVal < 0 : minVal = 0
    if maxVal > 100 : maxVal = 100
    if size > 30 or size < 3 : size = 25
    if minVal > maxVal : minVal, maxVal = maxVal, minVal


    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))
    
    drawData(data)

# Frames & Canvas 
# Row 0 
UserInterface = Frame(mainWindow, bg="black")
UserInterface.grid(row=0, column=0, padx=15, pady=5)
MainCanvas = Canvas(mainWindow, bg="white", width=600, height=380)
MainCanvas.grid(row=2, column=0, padx=10, pady=5)

SelectLbl = Label(UserInterface, text="Select Algorithm", bg="black", fg="white")
SelectLbl.grid(row=0, column=0, padx=5, pady=5, sticky=W)
AlgMenu = ttk.Combobox(UserInterface, textvariable=selected_alg, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"], state="readonly")
AlgMenu.grid(row=0, column=1, padx=5, pady=5)
AlgMenu.current(0)
GenerateBtn = Button(UserInterface, text="Generate Array", command=GenerateArray, bg="black", fg="white")
GenerateBtn.grid(row=0, column=2, padx=5, pady=5)

# Row 1
SizeLbl = Label(UserInterface, text="Size Value", bg="black", fg="white")
SizeLbl.grid(row=1, column=0, padx=5, pady=5, sticky=W)
SizeEntry = Entry(UserInterface)
SizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

minLbl = Label(UserInterface, text="Min Value", bg="black", fg="white")
minLbl.grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UserInterface)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

maxLbl = Label(UserInterface, text="Max Value", bg="black", fg="white")
maxLbl.grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UserInterface)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)




mainWindow.mainloop()

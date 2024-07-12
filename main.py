from tkinter import *
from tkinter import ttk
import numpy as np
import random 

mainWindow = Tk()
mainWindow.title("Sorting Algorithm Visualizer")
mainWindow.geometry("900x600")
mainWindow.config(bg="black")

# Variables
selected_alg = StringVar()

def drawData(data):
    a_height = 400
    a_width = 600
    x_width = a_width / (len(data) + 1)
    offset = 30
    spacing = 10
    for i, height in enumerate(data):
        # Top left
        x0 = i * x_width + offset + spacing
        y0 = a_height - height
        # Bottom right
        x1 = (i + 1) * x_width + offset
        y1 = a_height
        mainWindow.update



def GenerateArray():
    print('Alg Selected: ' + selected_alg.get())

# Frames & Canvas
# Row 0
UserInterface = Frame(mainWindow, bg="black")
UserInterface.grid(row=0, column=0, padx=15, pady=5)
MainCanvas = Canvas(UserInterface, bg="black", width=800, height=500)
MainCanvas.grid(row=0, column=0, padx=15, pady=5)
SelectLbl = Label(MainCanvas, text="Select Algorithm", bg="black", fg="white")
SelectLbl.grid(row=0, column=0, padx=5, pady=5, sticky=W)
AlgMenu = ttk.Combobox(MainCanvas, textvariable=selected_alg, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"], state="readonly")
AlgMenu.grid(row=0, column=1, padx=5, pady=5)
AlgMenu.current(0)
GenerateBtn = Button(MainCanvas, text="Generate Array", command=GenerateArray, bg="black", fg="white")
GenerateBtn.grid(row=0, column=2, padx=5, pady=5)

# Row 1
SizeLbl = Label(MainCanvas, text="Size Value", bg="black", fg="white")
SizeLbl.grid(row=1, column=0, padx=5, pady=5, sticky=W)
SizeEntry = Entry(MainCanvas)
SizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

minLbl = Label(MainCanvas, text="Min Value", bg="black", fg="white")
minLbl.grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(MainCanvas)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

maxLbl = Label(MainCanvas, text="Max Value", bg="black", fg="white")
maxLbl.grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(MainCanvas)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)




mainWindow.mainloop()

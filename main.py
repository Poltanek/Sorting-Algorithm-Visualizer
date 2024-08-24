from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort

# Main Window setup
mainWindow = Tk()
mainWindow.title("Sorting Algorithm Visualizer")
mainWindow.geometry("1000x600")
mainWindow.config(bg="black")

# Variables
selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    MainCanvas.delete("all")
    a_height = 380
    a_width = 600
    x_width = a_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = a_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = a_height
        MainCanvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
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

    data = [random.randint(minVal, maxVal) for _ in range(size)]
    drawData(data, ["red" for _ in range(len(data))])

def StartAlgorithm():
    global data
    speed = SpeedScale.get()
    
    if selected_alg.get() == "Bubble Sort":
        bubble_sort(data, drawData, speed)
    if selected_alg.get() == "Selection Sort":
        pass
    if selected_alg.get() == "Insertion Sort":
        pass
    if selected_alg.get() == "Merge Sort":
        merge_sort(data, drawData, speed)
    if selected_alg.get() == "Quick Sort":
        pass
    if selected_alg.get() == "Heap Sort":
        pass

# ---------- UI Setup ----------
UserInterface = Frame(mainWindow, bg="grey")
UserInterface.grid(row=0, column=0, padx=15, pady=5)
MainCanvas = Canvas(mainWindow, bg="grey", width=600, height=380)
MainCanvas.grid(row=2, column=0, padx=10, pady=5)

# ---------- Widgets ----------
SelectLbl = Label(UserInterface, text="Select Algorithm", bg="black", fg="white")
SelectLbl.grid(row=0, column=0, padx=5, pady=5, sticky=W)
ComboBox = ttk.Combobox(UserInterface, textvariable=selected_alg, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"], state="readonly")
ComboBox.grid(row=0, column=1, padx=5, pady=5)
ComboBox.current(0)

GenerateArrayBtn = Button(UserInterface, text="Generate Array", command=GenerateArray, bg="black", fg="white")
GenerateArrayBtn.grid(row=0, column=2, padx=5, pady=5)

SpeedScale = Scale(UserInterface, from_=0.1, to=2.0, bg="black", fg="white", length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
SpeedScale.grid(row=0, column=3, padx=5, pady=5)

SizeEntry = Scale(UserInterface, from_=3, to=30, bg="black", fg="white", length=200, resolution=1, orient=HORIZONTAL, label="Select Size")
SizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

minEntry = Scale(UserInterface, bg="black", fg="white", from_=0, to=10, length=200, resolution=1, orient=HORIZONTAL, label="Select Min Value")
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

maxEntry = Scale(UserInterface, bg="black", fg="white", from_=10, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Select Max Value")
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

startBtn = Button(UserInterface, command=StartAlgorithm, text="Start Sorting", bg="black", fg="white")
startBtn.grid(row=1, column=6, padx=5, pady=5)

mainWindow.mainloop()

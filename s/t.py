from tkinter.ttk import Treeview


try:
    from tkinter import * 
except ImportError:
    from tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Treeview(root, text="")
        b.grid(row=i, column=j)

mainloop()
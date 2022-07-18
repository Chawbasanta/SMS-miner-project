from struct import pack
from tkinter import*

win=Tk()
win.title("tile")
pic=PhotoImage(file='qrcode.png')
l=Label(win,image=pic,height=121,width=121)
l.pack()
win.mainloop()
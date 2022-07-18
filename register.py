from tkinter import *
from tkinter import ttk
from turtle import left
from PIL import Image,ImageTk

winregist=Tk()
winregist.geometry('700x370')
winregist.iconbitmap('ss.ico')
winregist.title('_register')
winregist.config(bg='#e5dde7')
imgregist=Image.open('img/regist.jpg')
imgregist=imgregist.resize((400,330))
imgreside=ImageTk.PhotoImage(imgregist)
registlabel=Label(winregist,image=imgreside)
registlabel.pack(side=LEFT)
winregist.mainloop()

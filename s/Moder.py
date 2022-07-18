from cProfile import label
from ctypes import HRESULT
#import imp
from operator import length_hint
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import*
from turtle import width
from matplotlib.pyplot import text

from pyrsistent import b
from setuptools import Command
from tensorboard import program
win=Tk()
win.title("Demo")
win.geometry('500x300')
s=ttk.Style()
s.theme_use('clam')
s.configure('red.Horizontal.TProgressbar',foreground='red',background='#4f4f4f4')
progress=Progressbar(win,style='red.Horizontal.TProgressbar',orient=HORIZONTAL,length=500,mode='determinate')
def main_win():
    win1=Tk()
    win1.geometry('427x250')
    label1=Label(win1,text='ADD TEXT HERE',fg='dark grey',bg=None)
    fontstyle=('calirbi(body)',24,'bold')
    label1.config(font=fontstyle)
    label1.place(x=80,y=100)
def bar():
    win2=Tk()
    label2=Label(win2,text='Loading....',fg='white',bg='#249794')
    fontstyle=('calibri(body)',10)
    label2.config(font=fontstyle)
    label2.place(x=0,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        win2.update_idletasks()
        time.sleep(0.03)
        r=r+1
    win2.destroy()
    main_win()
progress.place(x=-10,y=235)
Frame(win,width=427,height=241,bg='#249794').place(x=0,y=0)
b1=Button(win,width=10,text='Get started',Command=bar,fg='#249794')
b1.place(x=170,y=200)
l1=Label(win,text='Splash',fg='white',bg='#249794')
fonstyle=('calibri(body)',10,'bold')
l1.configure(font=fonstyle)
l1.place(x=50,y=80)
win.mainloop()


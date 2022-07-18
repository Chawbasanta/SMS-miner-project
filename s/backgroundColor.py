from ast import If
from tkinter import*
from tkinter import ttk

class Application(object):
    def __init__(self,win):
        self.win=win
        self.top=Frame(win,height=150,bg='white')
        self.top.pack(fill=X)
        self.bottom=Frame(win,height=600,bg='gray')
        self.bottom.pack(fill=X)

def main():
    win=Tk()
    win.title("APp")
    win.geometry('600x400')
    #win.resizable(False,False)
    app=Application(win)
    win.mainloop()
if __name__=='__main__':
    main()
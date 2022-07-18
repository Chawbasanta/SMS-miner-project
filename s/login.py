
from PIL import Image,ImageTk
from matplotlib import image
from matplotlib.ft2font import BOLD
from tkinter import *
import pyttsx3


def SignUp():
    if get_user.get()=='chaw' and get_pass.get()=='123':
        Speak('Successfully login !')
    elif get_pass.get()=="" and get_user.get()=="":
        Speak("Invalid password and user name")
    else:
        Speak('Unsuccessfully login ')
    
        
        
def Speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(audio)
    print(audio)
    print()
    engine.runAndWait()
    
def WishMe():
    import time,datetime
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak('Goood Morning have a you nice today ')
    elif hour >=12 and hour<18:
        Speak('Good Afternoon')
    elif hour>=18 and hour < 20:
        Speak('Good Evening')
    else:
        Speak('Goood night ')
        
def get_time():
    import time
    timevar=time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(200,get_time)
#Speak('hlo how are u darling')



win=Tk()
win.title('__login')
win.geometry('600x360')
win.config(bg='whitesmoke')


sideimage=Image.open('img/mg.jpg')
sideimage=sideimage.resize((300,370))
sideimg=ImageTk.PhotoImage(sideimage)
sidelabel=Label(win,image=sideimg).place(x=0,y=0)

registerButton=Button(win,text='REGISTER',relief=GROOVE,height=1,width=18,bd=0)
registerButton.place(x=222,y=290)
resetButton=Button(win,text='RESET PASSWORD',relief=GROOVE,height=1,width=18,bd=0)
resetButton.place(x=222,y=310)

clock=Label(win,width=12,height=1,font=('calibri',13))
clock.place(x=2,y=2)
get_time()

bottom=Frame(win,bg='pink',height=20,width=300)
bottom.pack(side=BOTTOM,fill=X)

license=Label(win,text='@Copyright 2023',bg='pink')
license.place(x=0,y=340)
dev=Label(win,text='@Developed by Chaw basanta',bg='pink')
dev.place(x=400,y=340)
adminimage=Image.open('img/ib.png',)
adminimage=adminimage.resize((100,105))
admin=ImageTk.PhotoImage(adminimage)
adminlabel=Label(win,image=admin).place(x=415,y=20)
student=Label(win,text='!! S T U D E N T !!').place(x=423,y=140)
get_user=StringVar()
get_pass=StringVar()
userlabel=Label(win,text='U S E R').place(x=340,y=180)
user=Entry(win,font=2,width=15,textvariable=get_user,bg='whitesmoke').place(x=400,y=180)
passlabel=Label(win,text='P A S S',).place(x=340,y=230)
password=Entry(win,font=2,width=15,textvariable=get_pass,bg='whitesmoke').place(x=400,y=230)
signUp=Button(win,text='S i g n U p',relief=GROOVE,command=SignUp).place(x=435,y=270)
win.resizable(False,False)
WishMe()
win.mainloop()
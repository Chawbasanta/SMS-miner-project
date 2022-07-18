from tkinter import *
import webbrowser
import pyttsx3
import datetime
from PIL import Image,ImageTk

#--------------------Social Link-----------------------
#https://github.com/Chawbasanta
#https://www.facebook.com/basantaChaw
#https://www.linkedin.com/in/basanta-chaw-15327a201/
#https://www.youtube.com/channel/UCF0bo_siMzdjxY_yMVrMypA
#https://twitter.com/Ibasanta69
def  facebook():
    webbrowser.open('https://www.facebook.com/basantaChaw')
def git():
    webbrowser.open('https://github.com/Chawbasanta')
def twitter():
    webbrowser.open('https://twitter.com/Ibasanta69')
def yt():
    webbrowser.open('https://www.youtube.com/channel/UCF0bo_siMzdjxY_yMVrMypA')
#------------------------------------------------------

def get_time():
    import time
    timevar=time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(200,get_time)

def Speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    engine.say(audio)
    print(audio)
    print()
    engine.runAndWait()

def WishMe():
   
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak('Goood Morning have a you nice today ')
    elif hour >=12 and hour<18:
        Speak('Good Afternoon')
    elif hour>=18 and hour < 20:
        Speak('Good Evening')
    else:
        Speak('Goood night ')
   
#--------------------Intial-------------------
winlogin=Tk()
winlogin.title('_Login')
winlogin.iconbitmap('img/ss.ico')
winlogin.geometry('600x360')
winlogin.config(bg='whitesmoke')
#WishMe()
#-----------------------------------------------

#----------------------IMage Show part------------------
sideimage=Image.open('img/mg.jpg')
sideimage=sideimage.resize((300,370))
sideimg=ImageTk.PhotoImage(sideimage)
sidelabel=Label(winlogin,image=sideimg).place(x=0,y=0)
adminimage=Image.open('img/admin.png',)
adminimage=adminimage.resize((100,105))
admin=ImageTk.PhotoImage(adminimage)
adminlabel=Label(winlogin,image=admin).place(x=415,y=20)

#------------------------------------------------------------


#--------------------Button Show Part--------------------------

registerButton=Button(winlogin,text='REGISTER',relief=GROOVE,height=1,width=18,bd=0)
registerButton.place(x=222,y=290)
resetButton=Button(winlogin,text='RESET PASSWORD',relief=GROOVE,height=1,width=18,bd=0)
resetButton.place(x=222,y=310)
 #---------------------------------------------------------
clock=Label(winlogin,width=12,height=1,font=('calibri',13))
clock.place(x=2,y=2)
get_time()
#-----------------------------------------------------------------------

#--------------------------------Social icons ----------------------------------
# ------------------Faceboook------------
facebookimg=Image.open('socialIcons/fb.png')
facebookimg=facebookimg.resize((30,30))
facebookimgp=ImageTk.PhotoImage(facebookimg)
facebookbtn=Button(winlogin,image=facebookimgp,bd=0,command=facebook)
facebookbtn.place(x=10,y=300)

#-------------------Twitter------------------
twitterimg=Image.open('socialIcons/tw.png')
twitterimg=twitterimg.resize((28,28))
twitterimgp=ImageTk.PhotoImage(twitterimg)
twitterbtn=Button(winlogin,image=twitterimgp,bd=0,command=twitter)
twitterbtn.place(x=50,y=300)

#----------------------Github------------------------------
gitimg=Image.open('socialIcons/git.png')
gitimg=gitimg.resize((30,30))
gitimgp=ImageTk.PhotoImage(gitimg)
gitbtn=Button(winlogin,image=gitimgp,bd=0,command=git)
gitbtn.place(x=90,y=300)



#-----------------------Youtube----------------------
ytimg=Image.open('socialIcons/yt.png')
ytimg=ytimg.resize((30,30))
ytimgp=ImageTk.PhotoImage(ytimg)
ytbtn=Button(winlogin,image=ytimgp,bd=0,command=yt)
ytbtn.place(x=140,y=300)

#--------------------------------------------------------------------------


#---------------------------------Label Shoiw Part--------------------------
student=Label(winlogin,text='!! S T U D E N T !!').place(x=423,y=140)
get_user=StringVar()
get_pass=StringVar()
userlabel=Label(winlogin,text='U S E R').place(x=340,y=180)
user=Entry(winlogin,font=2,width=15,textvariable=get_user,bg='whitesmoke').place(x=400,y=180)
passlabel=Label(winlogin,text='P A S S',).place(x=340,y=230)
password=Entry(winlogin,font=2,width=15,textvariable=get_pass,bg='whitesmoke').place(x=400,y=230)
signUp=Button(winlogin,text='S i g n U p',relief=GROOVE).place(x=435,y=270)


#-----------------------Footer Part Show -----------------------
bottom=Frame(winlogin,bg='pink',height=20,width=300)
bottom.pack(side=BOTTOM,fill=X)

license=Label(winlogin,text='@Copyright 2023',bg='pink')
license.place(x=0,y=340)
dev=Label(winlogin,text='@Developed by Chaw basanta',bg='pink')
dev.place(x=400,y=340)
#--------------------------------------------------------------
winlogin.resizable(False,False)
winlogin.mainloop()
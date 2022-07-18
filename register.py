from tkinter import *
import webbrowser
from PIL import Image,ImageTk

winregist=Tk()
winregist.geometry('700x350')
winregist.iconbitmap('img/ss.ico')
winregist.title('_register')
winregist.config(bg='whitesmoke')
imgregist=Image.open('img/regist.jpg')
imgregist=imgregist.resize((400,300))
imgreside=ImageTk.PhotoImage(imgregist)
registlabel=Label(winregist,image=imgreside)
registlabel.pack(side=LEFT)

#---------------------------Database Connection Part------------------------------------
def mysqlregister():
    import mysql.connector as mq
    
    conn=mq.connect(host='localhost',user='root',password='',database='dbsms')
    curs=conn.cursor()
    fname_sms=fnames.get()
    lname_sms=lnames.get()
    email_sms=emails.get()
    addres_sms=addresses.get()
    contact_sms=contacts.get()
    password_sms=passwords.get()
    confirmpassword_sms=confirmpasswords.get()
    sex_sms=sex.get()
    print(fname_sms)
    print()
    print(lname_sms)
    print()
    print(email_sms)
    print()
    print(sex_sms)
    print()
    print(addres_sms)
    print()
    print(contact_sms)
    print()
    print(password_sms)
    print()
    print(confirmpassword_sms)
    
    if sex_sms==1:
        male='male'
        sql=('insert into regist(fname,lname,email,sex,pass,con_pass,address,contact) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(fname_sms, lname_sms,email_sms,male,password_sms,confirmpassword_sms,addres_sms,contact_sms)) 
        if(conn.is_connected()):
            curs.execute(sql)
            conn.commit()
            print('Successfully Inserted Data !')
        else:
            print('Unsucessfully Inserted Data !')
            curs.close()
            conn.close()
    else:
        female='female'
        sql=('insert into register(fname,lname,email,sex,pass,con_pass,address,contact) values("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(fname_sms,lname_sms,email_sms,female,password_sms,confirmpassword_sms,addres_sms,contact_sms))
        if(conn.is_connected()):
            curs.execute(sql)
            conn.commit()
            print('Successfully Inserted Data !')
        else:
            print('Unsucessfully Inserted Data !')
            curs.close()
            conn.close()


  


#--------------------------------------------------------------
def clearEnrty():
    fname.delete(0,END)
    lname.delete(0,END)
    email.delete(0,END)
    password.delete(0,END)
    confirmpassword.delete(0,END)
    address.delete(0,END)
    contact.delete(0,END)
    

def get_time():
    import time
    timevar=time.strftime("%I:%M:%S  %p")
    clock.config(text=timevar)
    clock.after(200,get_time)
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
#---------------------Dataget--------------------
def getdata():
    print(fnames.get())
    print()
    print(lnames.get())
    print()
    print(emails.get())
    print()
    print(addresses.get())
    print()
    print(contacts.get())
    print()
    print(passwords.get())
    print(confirmpasswords.get())
    if sex.get()==1:
        print('Male')
    else:
        print('Female')


#-------------------------------

#--------------------------------Social icons ----------------------------------
# ------------------Faceboook------------
facebookimg=Image.open('socialIcons/fb.png')
facebookimg=facebookimg.resize((20,20))
facebookimgp=ImageTk.PhotoImage(facebookimg)
facebookbtn=Button(winregist,image=facebookimgp,bd=0,command=facebook)
facebookbtn.place(x=120,y=326)

#-------------------Twitter------------------
twitterimg=Image.open('socialIcons/tw.png')
twitterimg=twitterimg.resize((18,18))
twitterimgp=ImageTk.PhotoImage(twitterimg)
twitterbtn=Button(winregist,image=twitterimgp,bd=0,command=twitter)
twitterbtn.place(x=160,y=326)

#----------------------Github------------------------------
gitimg=Image.open('socialIcons/git.png')
gitimg=gitimg.resize((20,20))
gitimgp=ImageTk.PhotoImage(gitimg)
gitbtn=Button(winregist,image=gitimgp,bd=0,command=git)
gitbtn.place(x=200,y=326)


#-------------------------Clock----------------
clock=Label(winregist,width=12,height=1,font=('Helavatic',12,'bold'),fg='#1f1f1f',bg='whitesmoke')
clock.place(x=150,y=0)
get_time()
#-------------


#-----------------------Youtube----------------------
ytimg=Image.open('socialIcons/yt.png')
ytimg=ytimg.resize((20,20))
ytimgp=ImageTk.PhotoImage(ytimg)
ytbtn=Button(winregist,image=ytimgp,bd=0,command=yt)
ytbtn.place(x=250,y=326)

#-----------------------Footer Part Show -----------------------
bottom=Frame(winregist,bg='#59547a',height=20,width=300)
bottom.pack(side=BOTTOM,fill=X)

# license=Label(bottom,text='@Copyright 2023',bg='#59547a',fg='white')
# license.place(x=0,y=330)
dev=Label(winregist,text='@Developed by Chaw basanta',bg='#59547a',fg='white')
dev.place(x=460,y=330)
#--------------------------------------------------------------

#----------------------Entrybox-0----------------------------
fnames=StringVar()
lnames=StringVar()
sex=IntVar()
emails=StringVar()
passwords=StringVar()
confirmpasswords=StringVar()
addresses=StringVar()
contacts=StringVar()

sms=Label(winregist,text='S T U D E N T    M S',font=('Monospace',15,'bold'),fg='#75acf0')
sms.place(x=50,y=100)

student=Label(winregist,text='S T U D E N T  R E G I S T E R',font=('Helavatic',13,'bold'),fg='#75acf0')
student.place(x=50,y=133)
fnamelb=Label(winregist,text='f i r s t     n a m e')
fnamelb.place(x=420,y=45)
fname=Entry(winregist,textvariable=fnames)
fname.place(x=420,y=70)

lnamelb=Label(winregist,text='l a s t     n a m e')
lnamelb.place(x=560,y=45)
lname=Entry(winregist,textvariable=lnames)
lname.place(x=560,y=70)


emaillb=Label(winregist,text='e m a i l   i d')
emaillb.place(x=420,y=105)
email=Entry(winregist,textvariable=emails,width=30)
email.place(x=420,y=130)
#---------------------Radio button ------------------------------
malelb=Label(winregist,text='male')
malelb.place(x=612,y=105)
male=Radiobutton(winregist,value=1,variable=sex)
male.place(x=620,y=125)

malelb=Label(winregist,text='female')
malelb.place(x=650,y=105)
female=Radiobutton(winregist,value=0,variable=sex)
female.place(x=660,y=125)

#-------------------------------------------------------
#---------------------Passwords field--------------------

passwordlb=Label(winregist,text='p a s s w o r d')
passwordlb.place(x=420,y=160)
password=Entry(winregist,textvariable=passwords,show='*')
password.place(x=420,y=185)

confirmpasswordlb=Label(winregist,text='c o n f   p a s s w o r d')
confirmpasswordlb.place(x=560,y=160)
confirmpassword=Entry(winregist,textvariable=confirmpasswords,show='*')
confirmpassword.place(x=560,y=185)


#------------------------------------------------------
addresslb=Label(winregist,text='a d d r e s s  ')
addresslb.place(x=420,y=215)
address=Entry(winregist,textvariable=addresses,width=25)
address.place(x=420,y=240)
contactlb=Label(winregist,text='c o n t a c t  ')
contactlb.place(x=590,y=215)
contact=Entry(winregist,width=15,textvariable=contacts)
contact.place(x=590,y=240)
#--------------------------Button--------------------- 

clearbutton=Button(winregist,text='C l e a r',width=17,relief=GROOVE,font=('Helavatic',9,'bold'),bg='#ff7163',command=clearEnrty)
clearbutton.place(x=420,y=280)

submit=Button(winregist,text='S u b m i t',width=17,relief=GROOVE,font=('Helavatic',9,'bold'),bg='#6ecb6f',command=mysqlregister)
submit.place(x=560,y=280)

#-----------------------------------------------


winregist.resizable(False,False)
winregist.mainloop()

from tkinter import *

import json

def login():
    
    uname=txt1.get()
    pword=txt2.get()
    try:
        with open('d:/insta.json') as f:
            dct=json.load(f)
            if uname in dct:
                if(dct[uname]==pword):
                    lbl_result.configure(text="Welcome!")
                else:
                    lbl_result.configure(text="Wrong Password!")
            elif(uname=="" and pword==""):
                lbl_result.configure(text="Enter The User And Password!")                
            else:
                lbl_result.configure(text="User Not Exist!")
    except FileNotFoundError:
        lbl_result.configure(text="File Didn't Find!")
def submit():
    
    try:
        uname=txt1.get()
        pword=txt2.get()
        with open('d:/insta.json') as f:
            dct=json.load(f)
        if uname in dct:
            lbl_result.configure(text="User Aleady Exist!")
        elif(uname=="" and pword==""):
                lbl_result.configure(text="Enter The User And Password!")  
        else:
            dct[uname]=pword
            with open('d:/insta.json','w') as f:
                json.dump(dct,f)
            lbl_result.configure(text="Submit Done!")
    except FileNotFoundError:
        lbl_result.configure(text="File Didn't Find!")
        
def delete():
    
    try:
        uname=txt1.get()
        pword=txt2.get()
    
        with open('d:/insta.json') as f:
            dct=json.load(f)
        if uname in dct:
            if(dct[uname]==pword):
                dct.pop(uname)
                with open('d:/insta.json','w') as f:
                    json.dump(dct,f)
                lbl_result.configure(text="Your Account Deleted!")
            else:
                lbl_result.configure(text="Wrong Password!")
        elif(uname=="" and pword==""):
                lbl_result.configure(text="Enter The User And Password!")  
        else:
            lbl_result.configure(text="User Not Exist!")
    except FileNotFoundError:
        lbl_result.configure(text="File Didn't Find!")


win=Tk()
win.title('Instagram')

win.geometry("248x350")
win.resizable(False,False)

win.rowconfigure([0,1],weight=0)
win.columnconfigure(0,weight=0)


lbl1=Label(master=win,text="Username:",font=('none',15))
lbl1.grid(row=0,column=0)

txt1=Entry(win,width=14)
txt1.grid(row=4,column=0)


lbl2=Label(master=win,text="Password:",font=('none',15))
lbl2.grid(row=6,column=0)


txt2=Entry(win,width=14)
txt2.grid(row=8,column=0)


lbl69=Label(master=win,text="     ",font=('none',15))
lbl69.grid(row=10,column=0)



btn=Frame(master=win,height=60,bg='black')

btn.rowconfigure(0,weight=1)
btn.columnconfigure([0,1,2],weight=1)

lbtn=Button(master=btn,text="Login",height=3,
            font=("None",15,"bold"),command=login).grid(row=0,column=0,
                                          sticky="nwes",padx=2,pady=4)
                                          
lbtn=Button(master=btn,text="Submit",height=3,
            font=("None",15,"bold"),command=submit).grid(row=0,column=1,
                                          sticky="nwes",padx=2,pady=3)
                                          
lbtn=Button(master=btn,text="Delete",height=3,
            font=("None",15,"bold"),command=delete).grid(row=0,column=2,
                                          sticky="nwes",padx=2,pady=4)
                                          
btn.grid(row=16,column=0,sticky="wen")


lbl_result=Label(master=win,font=('none',13),
                 text="Enter The User And Password!")
lbl_result.grid(column=0,row=18)


win.mainloop()
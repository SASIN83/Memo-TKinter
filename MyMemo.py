#Importing libraries
from os import path
from tkinter import *
import os
import tkinter

#Getting current working directory
mpath=os.path.dirname(os.path.realpath(__file__))
#Changing the directory to current directory
os.chdir(mpath)

#Saving the Memo
def saved():
    screen8=Toplevel(screen)
    screen8.title("Saved")
    screen8.geometry("100x100")
    Label(screen8,text="Saved").pack()
    Button(screen8, text="OK",command=screen8.destroy).pack()
def save():
    filename=r_filename.get()
    notes=r_notes.get()

    data=open(filename,"w")
    data.write(notes)
    data.close()

    saved()

#Creating Memo
def create_note():
    try:
        os.mkdir(username1)
        os.chdir(username1)
    except:
        os.chdir(username1)
    global r_filename
    global r_notes
    r_filename = StringVar()
    r_notes = StringVar()

    screen7 = Toplevel(screen)
    screen7.title("Happy memo")
    screen7.geometry("250x200")
    Label(screen7,text="Please Enter File Name: ").pack()
    Entry(screen7,textvariable=r_filename).pack()
    Label(screen7,text="Write Something").pack()
    Entry(screen7,textvariable=r_notes).pack()
    Button(screen7,text="Save", command=save).pack()

#Deleting screen 12 and 13
def del_note2A():
    screen13.destroy()
    screen12.destroy()

def del_note2():
    global screen13
    screen13=Toplevel(screen)
    screen13.title("Well...")
    screen13.geometry("200x250")
    data2= r_filename2.get()
    delete=os.remove(data2)
    Label(screen13, text = "Your File Is Destroyed", fg="tomato").pack()
    Button(screen13, text= "OK", fg="green",command=del_note2A).pack()

def del_note3():
    screen12.destroy()


def del_note1():
    global screen12
    screen12=Toplevel(screen)
    screen12.title("Alert")
    screen12.geometry("250x300")
    screen11.destroy()
    Label(screen12, text="Are You Sure??").pack()
    Button(screen12, text="Yes", command=del_note2).pack(padx=5,pady=5)
    Button(screen12, text="No", command=del_note3).pack(padx=5,pady=5)

def del_note():
    global screen11
    screen11=Toplevel(screen)
    screen11.title("Delete Notes")
    screen11.geometry("250x300")
    all_files=os.listdir()
    Label(screen11,text="choose a file to see...").pack()
    Label(screen11,text=all_files).pack()
    global r_filename2
    r_filename2 = StringVar()
    Entry(screen11, textvariable=r_filename2).pack()
    Button(screen11,text="Delete Note",command=del_note1).pack()

#Viewing the file created
def view_note1():
    filename1= r_filename1.get()
    data = open(filename1,"r")
    data1=data.read()
    screen10=Toplevel(screen)
    screen10.title("Lets see your memo...")
    screen10.geometry("400x450")
    Label(screen10,text=data1).pack()

def view_note():
    screen9=Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("250x300")
    all_files=os.listdir()
    Label(screen9,text="choose a file to see...").pack()
    Label(screen9,text=all_files).pack()
    global r_filename1
    r_filename1 = StringVar()
    Entry(screen9, textvariable=r_filename1).pack()
    Button(screen9,command=view_note1,text="Open").pack()

#Logging out
def logout():
    os.chdir(mpath)
    Label(screen,text="Your Session Is Over, Thank You",fg="green").pack()
    screen6.destroy()


#DashBoard
def session():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.geometry("200x350")
    screen3.destroy()
    Button(screen6,text="Log Out", height=3,width=10, command=logout,font="Poppins 7").pack(side=BOTTOM,expand=1)
    Button(screen6,text="Create Memo",bg="sky blue",height=3,width=300,command=create_note,font="Poppins 8").pack(padx=3,pady=10,expand=0)
    Button(screen6,text="View Memo",bg="green2",height=3,width=300,command=view_note,font="Poppins 8").pack(padx=3,pady=10,expand=0)
    Button(screen6,text="Delete Memo",bg="firebrick2",height=3,width=300,command=del_note,font="Poppins 8").pack(padx=3,pady=10,expand=0)

#Destroying screen 4 and 5
def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

#Login verification
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Welcome")
    screen3.geometry("150x100")
    Label(screen3, text="Login success",font=("times new roman", 11)).pack()
    Button(screen3, text="OK", command=session).pack()

def password_incorrect():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Welcome")
    screen4.geometry("150x100")
    Label(screen4, text="Incorrect Passoword!!",bg="tomato",font=("times new roman", 11)).pack()
    Button(screen4, text="OK", command=delete3).pack()

def no_user():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Welcome")
    screen5.geometry("150x100")
    Label(screen5, text="No Such User Found!!",bg="tomato",font=("times new roman", 11)).pack()
    Button(screen5, text="OK", command=delete4).pack()


#Registering and checking for existing username
def register_user():

    username_info = username.get()
    password_info = password.get()
    x=os.listdir(mpath)

    if "Users" in x:
        os.chdir("Users")
    
    else:
        os.mkdir("Users")
        os.chdir("Users")

    x=os.listdir()
    
    if username_info in x:
        l="Username Already used !!!"
        l1.config(text=l)
        
        os.chdir(mpath)
        
    else:
        if len(username_info)!=0:
            with open(username_info, "w") as f:
                f.write(f'{username_info}\n{password_info}\n')
                f.close()
                l="Registered Successfully"
                l1.config(text=l)

        else:
            l=f"Empty Blocks"
            l1.config(text=l)
        
                      
         
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        os.chdir(mpath)



    

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_file = os.listdir("D:/PROJECTS/register/Users")
    if username1 in list_file:
        os.chdir("Users")
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            password_incorrect()

    else:
        no_user()
    
    os.chdir("..")
    try:
        os.mkdir("Memos")
        os.chdir("Memos")
    
    except:
        os.chdir("Memos")
    
    screen2.destroy()

def register():
    global screen1
    global l1
    screen1 = Toplevel(screen)
    screen1.title("REGISTER")
    screen1.geometry("700x250")
    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Enter your details").pack()
    Label(screen1, text="  ").pack()
    Label(screen1, text= "Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text= "Password * ").pack()
    password_entry=Entry(screen1, textvariable= password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=12, height=2,command = register_user).pack()

    
    l1=Label(screen1, text="Click register", fg="gold", font=("times new roman",11))
    l1.pack()
#Login to the app
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below").pack()
    Label(screen2, text="  ").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Button(screen2, text="Login", width=12, height=2, command=login_verify).pack()

#Main login and register Screen
def m_screen ():
    global screen
    screen = Tk()
    screen.geometry("700x250")
    screen.title("Notes 1.0")
    Label(text="Happy Memo", bg="light goldenrod", height="3", width="400",font=("times new roman", 11)).pack()
    Label(text="").pack()
    button1=Button(text="Login", height="3", width="40",command=login)
    Label(text="").pack()
    button2=Button(text="Register", height="3", width="40",command=register)
    button1.pack()
    button2.pack()
    screen.mainloop()

m_screen()
 
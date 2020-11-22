from tkinter import *
import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo('Window title','IM not one you think')
ans= tkinter.messagebox.askquestion('Question 1','im sasin')

if ans=='yes':
    print("3==D")


root.mainloop()
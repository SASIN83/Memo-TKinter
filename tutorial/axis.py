from tkinter import *
root = Tk()

one=Label(root, text='one', bg='yellow',fg='red')
two=Label(root, text='two', bg='blue',fg='yellow')
one.pack()
two.pack(fill=X)
three=Label(root, text='three', bg='green', fg='black')
three.pack(side=LEFT,fill=Y)
root.mainloop()
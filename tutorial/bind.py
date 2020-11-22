from tkinter import *
root = Tk()

def Name(event):
    print('im sasin')

#use command to bind or add event on def and use .bind
button1= Button(root, text='my name')
button1.bind('<Button-1>',Name)
button1.pack()
root.mainloop()
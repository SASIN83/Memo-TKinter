from tkinter import *
root = Tk()

def left(event):
    print('Left')
def mid(event):
    print('mid')
def right(event):
    print('right')

frame = Frame(root, width=300, height=350)

frame.bind('<Button-1>', left)
frame.bind('<Button-2>', mid)
frame.bind('<Button-3>', right)

frame.pack()

root.mainloop()
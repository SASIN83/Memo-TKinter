from tkinter import *

def dont():
    print('dododo')

root = Tk()

menu= Menu(root)
root.config(menu=menu)

smenu=Menu(menu)
menu.add_cascade(label='File', menu=smenu)
smenu.add_command(label='new pro..', command=dont)
smenu.add_command(label='new', command=dont)
smenu.add_separator()
smenu.add_command(label='exit', command=dont)

edit= Menu(menu)
menu.add_cascade(label='Edit', menu = edit)
edit.add_command(label='redo', command=dont)

#tools

tools= Frame(root,bg='yellow')
insertButt = Button(tools, text='insert Image',command=dont)
insertButt.pack(side=LEFT,padx=3, pady=2)
printButt = Button(tools, text='insert Image',command=dont)
printButt .pack(side=LEFT, padx=3,pady=3)

tools.pack(side=TOP, fill=X)

#status
status=Label (root,text='i dont do anything',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)
root.mainloop()
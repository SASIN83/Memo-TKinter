from tkinter import *
root = Tk()

username=Label(root, text='Name')
password=Label(root, text='Password')
entry_1= Entry(root)
entry_2= Entry(root)

#sticky doesnt take left right.. its directional
username.grid(row=0, sticky=E)
password.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

cb = Checkbutton(root,text='KEEP ME LOGGED IN.')
cb.grid(columnspan=2)

root.mainloop()
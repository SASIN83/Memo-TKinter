from tkinter import *

#frame.quit works for quitting frame
class butts:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.button1 = Button(frame, text="printmessage", command=self.message)
        self.button1.pack(side=LEFT)
        self.quit=Button(frame, text="Quit", command=frame.quit)
        self.quit.pack(side=LEFT)

    def message(self):
        print("it works")



root = Tk()
b=butts(root)
root.mainloop()
from tkinter import *
import time

root = Tk()



def myClick():
    for i in range(10):
        mylabel = Label(root,text="hello " + e.get())
        mylabel.pack()
        # time.sleep(1)

mybutton = Button(root, text="Enter you name: ",padx=50, command=myClick, fg='blue', bg='pink' )
mybutton.pack()

e = Entry(root,width=50, bg="pink")
e.pack()
e.get
e.insert(0,"enter you name")

root.mainloop()
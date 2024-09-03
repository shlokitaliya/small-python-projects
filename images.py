from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("shlok italiya")
root.iconbitmap("./favicon.ico")

my_img = ImageTk.PhotoImage(Image.open("calc.png"))
my_label = Label(image=my_img).pack()
 














button_quit = Button(root,command=root.quit,padx=20,pady=20,text="quit").pack()

root.mainloop()
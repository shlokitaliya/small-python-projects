from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=45, borderwidth=3)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10,)


sum = 0
def button_click(number):
    # e.delete(0,END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

def button_clear():
    e.delete(0, END)

def button_add():
    First_number = e.get()
    global f_num 
    global math
    math = "add"
    f_num = int(First_number)
    e.delete(0,END)



def button_sub():
    First_number = e.get()
    global f_num 
    global math
    math = "sub"
    f_num = int(First_number)
    e.delete(0,END)
    
def button_mul():
    First_number = e.get()
    global f_num 
    global math
    math = "mul"
    f_num = int(First_number)
    e.delete(0,END)
def button_div():
    First_number = e.get()
    global f_num 
    global math
    math = "div"
    f_num = int(First_number)
    e.delete(0,END)

def button_equal():
    global f_num
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(second_number))
    elif math == "sub":
        e.insert(0, f_num - int(second_number))
    elif math == "mul":
        e.insert(0, f_num * int(second_number))
    elif math == "div":
        e.insert(0, f_num / int(second_number))
    else:
        e.insert(0, "Error")
    
    
    # e.insert(0, f_num + int(second_number))


button_1 = Button(root, text="1", padx=40, pady=20, bg="pink", command=lambda: button_click(1)).grid(row=3,column=1)
button_2 = Button(root, text="2", padx=40, pady=20, bg="pink", command=lambda: button_click(2)).grid(row=3,column=2)
button_3 = Button(root, text="3", padx=40, pady=20, bg="pink", command=lambda: button_click(3)).grid(row=3,column=3)

button_4 = Button(root, text="4", padx=40, pady=20, bg="pink", command=lambda: button_click(4)).grid(row=2,column=1)
button_5 = Button(root, text="5", padx=40, pady=20, bg="pink", command=lambda: button_click(5)).grid(row=2,column=2)
button_6 = Button(root, text="6", padx=40, pady=20, bg="pink", command=lambda: button_click(6)).grid(row=2,column=3)

button_7 = Button(root, text="7", padx=40, pady=20, bg="pink", command=lambda: button_click(7)).grid(row=1,column=1)
button_8 = Button(root, text="8", padx=40, pady=20, bg="pink", command=lambda: button_click(8)).grid(row=1,column=2)
button_9 = Button(root, text="9", padx=40, pady=20, bg="pink", command=lambda: button_click(9)).grid(row=1,column=3)

button_0 = Button(root, text="0", padx=40, pady=20, bg="pink", command=lambda: button_click(0)).grid(row=4,column=1)
button_clear = Button(root, text="Clear", padx=80, bg="pink", pady=20, command=button_clear).grid(row=4,column=2, columnspan=2)
button_add = Button(root, text="+", padx=39, pady=20, bg="pink", command=button_add).grid(row=5,column=1)
button_equal = Button(root, text="=", padx=89, pady=20, bg="pink", command=button_equal).grid(row=5,column=2, columnspan=2)


button_sub = Button(root, text="-", padx=41, pady=20, bg="pink", command=button_sub).grid(row=6,column=1)
button_mul = Button(root, text="*", padx=40, pady=20, bg="pink", command=button_mul).grid(row=6,column=2)
button_div = Button(root, text="/", padx=39, pady=20, bg="pink", command=button_div).grid(row=6,column=3)

root.mainloop()

from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry

# ==================================================Settings=====================
root = Tk()
root.geometry("400x210")
root.resizable(width=False, height=False)

# ==================================================Variables=====================

value = 0
num1 = StringVar()
num2 = StringVar()
res = StringVar()


# ==================================================Frames========================
frame1 = Frame()
frame1.pack(fill=X)

frame2 = Frame()
frame2.pack(fill=X)

frame3 = Frame()
frame3.pack(fill=X)

frame4 = Frame()
frame4.pack(fill=X)
# ==================================================Functions======================


def errorMsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
    elif msg == 'divisionerror':
        tkinter.messagebox.showerror('Division Error', 'The value of input number 2 is 0. No dividing by 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def div():
    # checks if user is trying to divide by zero
    if num2.get() == '0':
        errorMsg('divisionerror')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res.set(value)
        except:
            errorMsg('error')


# ==================================================Buttons=================

btn_plus = Button(frame3, text="+", width=8, command=plus)
btn_plus.pack(side=LEFT, anchor=N, padx=5, pady=5)

btn_minus = Button(frame3, text="-", width=8, command=minus)
btn_minus.pack(side=LEFT, anchor=N, padx=5, pady=5)

btn_mul = Button(frame3, text="*", width=8, command=mul)
btn_mul.pack(side=LEFT, anchor=N, padx=5, pady=5)

btn_div = Button(frame3, text="/", width=8, command=div)
btn_div.pack(side=LEFT, anchor=N, padx=5, pady=5)

# ==================================================Entry================

first_num = Entry(frame1, textvariable=num1)
first_num.pack(fill=X, padx=5, expand=True)

second_num = Entry(frame2, textvariable=num2)
second_num.pack(fill=X, padx=5, expand=True)

result = Entry(frame4, textvariable=res)
result.pack(fill=X, padx=5, expand=True)
# ==================================================Labels==============

label_first_num = Label(frame1, text="Input Number 1 :", width=15)
label_first_num.pack(side=LEFT, padx=5, pady=5)


label_second_num = Label(frame2, text="Input Number 2 :", width=15)
label_second_num.pack(side=LEFT, padx=5, pady=5)


label_third_num = Label(frame4, text="Result :", width=10)
label_third_num.pack(side=LEFT, padx=5, pady=5)


root.mainloop()







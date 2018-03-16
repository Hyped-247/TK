from tkinter import *
import tkinter.messagebox


# ==================================================Settings=====================
root = Tk()
root.title('Cal')
root.geometry("400x150")
color = 'gray55'
root.configure(bg=color)
root.resizable(width=False, height=False)

# ==================================================Variables=====================
num1 = StringVar()
num2 = StringVar()
res = StringVar()


# ==================================================Frames========================
top_first = Frame(root, width=800, height=60, bg=color)
top_first.pack(side=TOP)
top_second = Frame(root,  width=800, height=60, bg=color)
top_second.pack(side=TOP)
top_third = Frame(root, width=800, height=60, bg=color)
top_third.pack(side=TOP)
top_fourth = Frame(root, width=800, height=60, bg=color)
top_fourth.pack(side=TOP)

# ==================================================Functions======================


def errorMsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
    elif msg == 'divisionerror':
        tkinter.messagebox.showerror('Division Error', 'Cannot divide by 0')


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

# ==================================================Button=================


btn_plus = Button(top_third, text="+", width=8, command=plus, highlightbackground=color)
btn_plus.pack(side=LEFT,  padx=5, pady=5)

btn_minus = Button(top_third, text="-", width=8, command=minus, highlightbackground=color)
btn_minus.pack(side=LEFT,  padx=5, pady=5)

btn_mul = Button(top_third, text="*", width=8, command=mul, highlightbackground=color)
btn_mul.pack(side=LEFT,  padx=5, pady=5)

btn_div = Button(top_third, text="/", width=8, command=div, highlightbackground=color)
btn_div.pack(side=LEFT,  padx=5, pady=5)

# ==================================================Entry+Labels================


label_first_num = Label(top_first, text="Input Number 1 :", bg=color)
label_first_num.pack(side=LEFT, padx=5, pady=5)
first_num = Entry(top_first, textvariable=num1, highlightbackground=color)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text="Input Number 2 :", bg=color)
label_second_num.pack(side=LEFT, padx=5, pady=5)
second_num = Entry(top_second, textvariable=num2, highlightbackground=color)
second_num.pack(side=LEFT)


label_third_num = Label(top_fourth, text="Result :", bg=color)
label_third_num.pack(side=LEFT, padx=5, pady=5)

result = Entry(top_fourth, textvariable=res, highlightbackground=color)
result.pack(side=LEFT)

root.mainloop()







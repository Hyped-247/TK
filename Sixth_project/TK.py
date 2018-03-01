from tkinter import *

root = Tk()
root.geometry('300x200')
root.resizable(width=False, height=False)

v = IntVar()
res = IntVar()
label = Label(root, text="Choose a Fruit:").place(x=100, y=3)

Radiobutton(root, text="Banana", padx=20, variable=v, value=1).place(x=5, y=30)
Radiobutton(root, text="Apple", padx=20, variable=v, value=2).place(x=5, y=50)
Radiobutton(root, text="Orange", padx=20, variable=v, value=3).place(x=5, y=70)


btn_cal = Button(root, text="Cal", command=lambda: cal())
btn_cal.place(x=5, y=150)

kg = Entry(root, width=20, bd=2, insertwidth=2)
kg.place(x=55, y=150)

Label(root, text="Result: ").place(x=5, y=120)
result = Entry(root, textvariable=res).place(x=60, y=120)


def cal():
    kg_int = int(kg.get())
    if v.get() == 1:
        res.set(kg_int * 3)
    elif v.get() == 2:
        res.set(kg_int * 5)
    elif v.get() == 3:
        res.set(kg_int * 7)


root.mainloop()

from tkinter import *
import smtplib
# ==================================================Settings=====================
root = Tk()
root.title("Run Python Code") # set up the title and size.
root.geometry('800x500')  # set up the size
root.configure(bg='gray32')
root.resizable(width=False, height=False)
# ==================================================Variables=====================

quality = IntVar()
color = 'gray32'

# ==================================================Frames========================
top = Frame(root, width=800, height=50, bg=color)
top.pack(side=TOP)
bottom = Frame(root, width=800, height=50, bg=color)
bottom.pack(side=BOTTOM)
left = Frame(root,  width=600, height=400, bg=color)
left.pack(side=LEFT)
right = Frame(root, width=250, height=400, bg=color)
right.pack(side=RIGHT)
# ==================================================Functions======================


def clear_text():
    message.delete("1.0", END)


def run():
    print(str(message.get("1.0", END)))
    eval(str(message.get("1.0", END)))


# ==================================================Buttons=================
btn_clear_from = Button(right, text="clear", font=('arial', 25, 'bold'), highlightbackground=color,
                        command=lambda: clear_text())
btn_clear_from.pack(side=TOP)

btn_clear_to = Button(right, text="Run", font=('arial', 25, 'bold'), highlightbackground=color, command=lambda: run())
btn_clear_to.pack(side=TOP)

# ==================================================Message================
message = Text(left, font=('arial', 20, 'bold'), bd=10, width=55, bg='gray80')
message.pack(side=TOP)

root.mainloop()

from tkinter import *
import tkinter.messagebox
from io import StringIO
# ==================================================Settings=====================
root = Tk()
root.title("Run Python Code")  # set up the title and size.
root.geometry('800x500')  # set up the size
color = 'gray32'
root.configure(bg=color)
root.resizable(width=False, height=False)
# ==================================================Frames========================
top = Frame(root, width=800, height=50, bg=color)
top.pack(side=TOP)
bottom = Frame(root, width=800, height=50, bg=color)
bottom.pack(side=BOTTOM)
# ==================================================Functions======================


def clear_text():
    message.delete("1.0", END)


def run():
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(message.get("1.0", END))
        sys.stdout = old_stdout
        tkinter.messagebox.showinfo("Result", redirected_output.getvalue())
    except SyntaxError:
        tkinter.messagebox.showinfo("Result", "SyntaxError: unexpected EOF while parsing")


# ==================================================Buttons=================
btn_clear_from = Button(top, text="clear", font=('arial', 25, 'bold'), highlightbackground=color,
                        command=lambda: clear_text())
btn_clear_from.pack(side=TOP)

btn_clear_to = Button(top, text="Run", font=('arial', 25, 'bold'), highlightbackground=color, command=lambda: run())
btn_clear_to.pack(side=TOP)

# ==================================================Message================
message = Text(bottom, font=('arial', 20, 'bold'), bd=10, width=88, bg='gray80')
message.pack(side=TOP)

root.mainloop()

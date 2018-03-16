from tkinter import *   # Not ready because cannot send mail.
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
# ==================================================Settings=====================
root = Tk()
root.title("Email Sender ")  # set up the title and size.
root.geometry('800x500')  # set up the size
color = 'gray32'
root.configure(bg=color)
root.resizable(width=False, height=False)
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


def clear_all():
    clear_from()
    clear_to()


def clear_from():
    f.delete(0, 'end')


def clear_to():
    t.delete(0, 'end')


def clear_text():
    message.delete("1.0", END)


def send(message):

    HOST = 'smtp.gmail.com'
    PORT = 465

    USERNAME = 'email@gmail.com'
    PASSWORD = 'pass'

    SENDER = 'email@gmail.com'
    RECIPIENT = 'email@gmail.com'

    text_subtype = 'plain'

    msg = MIMEText('text', text_subtype)

    msg['Subject'] = 'Python Script'
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    try:
        connection = SMTP(HOST, PORT)
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(SENDER, RECIPIENT, msg.as_string())
    except Exception as e:
        print(e)


# ==================================================Buttons=================
btn_clear_from = Button(right, text="clear from", font=('arial', 25, 'bold'),
                        highlightbackground=color,
                        command=lambda: clear_from())
btn_clear_from.pack(side=TOP)

btn_clear_to = Button(right, text="clear to", font=('arial', 25, 'bold'),
                      highlightbackground=color,
                      command=lambda: clear_to())
btn_clear_to.pack(side=TOP)

btn_send = Button(right, text="send", font=('arial', 25, 'bold'),
                  highlightbackground=color,
                  command=lambda: send(message))
btn_send.pack(side=BOTTOM)

btn_clear_all = Button(right, text="Clear all", font=('arial', 25, 'bold'),
                       highlightbackground=color,
                       command=lambda: clear_all())
btn_clear_all.pack(side=BOTTOM)

# ==================================================Labels==============
from_label = Label(top,  font=('arial', 20, 'bold'), text="From: ", bg=color)
from_label.place(x=10, y=10)

to_label = Label(top,  font=('arial', 20, 'bold'), text="To: ", bg=color)
to_label.place(x=400, y=10)

# ==================================================Entry================
f = Entry(top, font=('arial', 20, 'bold'), width=25, bd=8, insertwidth=2)
f.place(x=75, y=1)

t = Entry(top, font=('arial', 20, 'bold'), width=25, bd=8, insertwidth=2)
t.place(x=450, y=1)

# ==================================================Message================
message = Text(left, font=('arial', 20, 'bold'), bd=8, width=55)
message.pack(side=LEFT)

root.mainloop()

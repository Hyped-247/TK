from tkinter import *
from tkinter import filedialog

# ==================================================Settings=====================
root = Tk()
root.title("File Counter ")
color = 'gray77'
root.geometry('500x500')  # set up the size
root.configure(bg=color)
root.resizable(width=False, height=False)

# ==================================================Variables=====================
result = StringVar()
count_result = dict()

# ==================================================Function=====================


def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"),
                                                                                               ("all files", "*.txt")))


def clear():
    answer.delete("1.0", END)
    words_list.delete(0, END)


def count(file_text):
    if file_text:
        try:
            file = open(str(file_text), 'r')
            full_text = file.readlines()
            file.close()
            for word in words_list.get().split(', '):
                for text in full_text:
                    if word in count_result:
                        count_result[word] = count_result[word] + text.count(word)
                    else:
                        count_result[word] = text.count(word)
            answer.delete('1.0', END)
            for k, v in count_result.items():
                answer.insert(END, '{0} {1} \n'.format(k, v))
            count_result.clear()
        except:
            print('Something really bad just happened!')


# ==================================================Entry=====================

words_list = Entry(root, width=40, bd=2, insertwidth=2)
words_list.pack(fill=X)

# ==================================================Button=====================

first_file = Button(root, text="Select file", highlightbackground=color, width=58, command=lambda: open_file())
first_file.place(x=0, y=30)

count_txt = Button(root, text="Count Words", highlightbackground=color,  width=58, command=lambda: count(root.filename))
count_txt.place(x=0, y=60)

clear_txt = Button(root, text="Clear", highlightbackground=color,  width=58, command=lambda: clear())
clear_txt.place(x=0, y=90)

answer = Text(root, height=30, width=500, bg='gray83')
answer.place(x=0, y=120)

root.mainloop()

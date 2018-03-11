from tkinter import *
from tkinter import filedialog

# ==================================================Settings=====================
root = Tk()
root.title("File Counter ")
color = 'black'
root.geometry('500x500')  # set up the size
root.configure(bg=color)
root.resizable(width=False, height=False)

# ==================================================Variables=====================
result = StringVar()
count_result = dict()


def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.txt")))


def print_file():
    print(root.filename)


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

            for k, v in count_result.items():
                result.set('{0} {1} '.format(k, v))
            count_result.clear()
        except:
            print('Something really bad just happened!')


words_list = Entry(root, width=40, bd=2, insertwidth=2)
words_list.pack(fill=X)

first_f = Button(root, text="Select file: ", highlightbackground=color,
                 command=lambda: open_file())
first_f.place(x=0, y=30)

count_txt = Button(root, text="Count Words ", highlightbackground=color,
                   command=lambda: count(root.filename))
count_txt.place(x=0, y=60)

answer = Text(root, height=30, width=500)
answer.place(x=0, y=100)

root.mainloop()

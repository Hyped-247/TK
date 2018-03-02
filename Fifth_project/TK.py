from tkinter import Tk, Button, IntVar, Entry, E, StringVar, LEFT, TOP, W
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

root = Tk()
root.title("File Counter ")

first_f_count = IntVar()
first_s_count = IntVar()
words = StringVar()
count_result = dict()


def first_file():
     count(askopenfilename())


def second_file():
    count(askopenfilename())


def count(file):
    if file:
        try:
            file = open(str(file), 'r')
            full_text = file.readline()
            file.close()
            for word in words_list.get().split(','):  # mo
                for text in full_text:
                    if word in count_result:
                        count_result[word] = text.count(word)
                    else:
                        count_result[word] = count_result[word].get() + text.count(word)
            print(count_result)
        except:
            showerror("Open Source File", "Failed to read file\n'%s'" % file)
            return


words_list = Entry(root, width=40, bd=2, insertwidth=2)
words_list.pack(side=LEFT)

first_f = Button(root, text="Browse first File ", command=lambda: first_file())
first_f.pack(side=TOP, anchor=E)

second_f = Button(root, text="Browse second File ", command=lambda: second_file())
second_f.pack(side=TOP, anchor=E)


root.mainloop()

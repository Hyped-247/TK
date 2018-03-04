from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

root = Tk()
root.title("File Counter ")
color = 'black'
root.geometry('500x500')  # set up the size
root.configure(bg=color)
root.resizable(width=False, height=False)


first_f_count = IntVar()
first_s_count = IntVar()
words = StringVar()
count_result = dict()
txt_files = dict()


def create_file(file_number):
    txt_files[file_number] = askopenfilename()


def count():
    for k, v in txt_files.items():
        if v:
            try:
                file = open(str(v), 'r')
                full_text = file.readlines()
                file.close()
                for word in words_list.get().split(','):
                    for text in full_text:
                        if word in count_result:  # mo
                            count_result[word] = count_result[word].get() + text.count(word)
                        else:
                            count_result[word] = text.count(word)
                print(count_result)
            except:
                pass


words_list = Entry(root, width=40, bd=2, insertwidth=2)
words_list.pack(fill=X)

first_f = Button(root, text="First File ", highlightbackground=color, command=lambda: create_file(1))
first_f.place(x=0, y=30)

second_f = Button(root, text="Second File ", highlightbackground=color, command=lambda: create_file(2))
second_f.place(x=0, y=60)

third_f = Button(root, text="Third File ", highlightbackground=color, command=lambda: create_file(3))
third_f.place(x=0, y=90)

count_txt = Button(root, text="Count Files ", highlightbackground=color, command=lambda: count())
count_txt.place(x=400, y=90)


root.mainloop()

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

root = Tk()
root.title("File Counter ")
root.geometry('300x300')  # set up the size
root.resizable(width=False, height=False)


first_f_count = IntVar()
first_s_count = IntVar()
words = StringVar()
count_result = dict()


def first_file():
    return count(askopenfilename())


def second_file():
    return count(askopenfilename())


def count(file):
    if file:
        try:
            file = open(str(file), 'r')
            full_text = file.readline()
            file.close()
            for word in words_list.get().split(','):
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
words_list.pack(fill=X, padx=5, expand=True)

first_f = Button(root, text="First File ", command=lambda: first_file())
first_f.place(x=0, y=0)

second_f = Button(root, text="Second File ", command=lambda: second_file())
second_f.place(x=0, y=23)



root.mainloop()

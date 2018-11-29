import tkinter as tk
from tkinter import font as tkf
from tkinter import messagebox as msgbox


def labelConfig(lb, txt):
    lb.config(text=txt, fg="light green", bg="dark green")


def showMsgBox():
    msgbox.showinfo(ent.get(), "ent.get()")

x=0
def add (ent, y):
    global x
    x += y
    ent.delete(0,'end')
    ent.insert(tk.END, str(x))


root = tk.Tk()
default_font = tkf.nametofont("TkDefaultFont")
default_font.configure(size=56)
root.option_add("*Font", default_font)

ent = tk.Entry(root)
ent.grid(column=0, row=0, columnspan=2)

btnQuit = tk.Button(root, text="1", command=lambda: add(ent, 1))
btnQuit.grid(column=0, row=1, sticky = tk.W)

button2 = tk.Button(root, text= "2", command=lambda: add(ent, 2))
button2.grid(column=0, row=1, sticky = tk.E)

root.mainloop()

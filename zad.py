import tkinter as tk
from tkinter import font as tkf
from tkinter import messagebox as msgbox



root = tk.Tk()
default_font = tkf.nametofont("TkDefaultFont")
default_font.configure(size=56)
root.option_add("*Font", default_font)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
tk.Checkbutton(root, text="op1", variable=var1, command=lambda: print(var1.get())).grid(row=0, column=0)
tk.Checkbutton(root, text="op2", variable=var2, command=lambda: print(var2.get())).grid(row=1, column=0)
root.mainloop()

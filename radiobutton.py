import tkinter as tk
from tkinter import font as tkf
from tkinter import messagebox as msb



root = tk.Tk()
default_font = tkf.nametofont("TkDefaultFont")
default_font.configure(size=56)
root.option_add("*Font", default_font)
var=tk.IntVar()
tk.Radiobutton(root, text="op1", value=1, variable=var, command=lambda: print(var.get())).pack()
tk.Radiobutton(root, text="op2", value=2, variable=var, command=lambda: print(var.get())).pack()
var1=tk.IntVar()
tk.Radiobutton(root, text="op3", value=3, variable=var1, command=lambda: print(var1.get())).pack()
tk.Radiobutton(root, text="op4", value=4, variable=var1, command=lambda: print(var1.get())).pack()


root.mainloop()


import tkinter as tk
from tkinter import font as tkf
from tkinter import messagebox as msb



root = tk.Tk()
default_font = tkf.nametofont("TkDefaultFont")
default_font.configure(size=32)
root.option_add("*Font", default_font)

txtAr = tk.Text(root, height=10, width=30)
txtAr.pack(side=tk.LEFT, fill=tk.Y)
scroll = tk.Scrollbar(root)
scroll.config(command=txtAr.yview)
txtAr.config(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)


root.mainloop()
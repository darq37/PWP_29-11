import tkinter as tk
from tkinter import font as tkf
from tkinter import messagebox as msb

root = tk.Tk()
default_font = tkf.nametofont("TkDefaultFont")
default_font.configure(size=32)
root.option_add("*Font", default_font)

cnv=tk.Canvas(root, width=300, height=300)
cnv.pack()
cnv.create_line(30, 20,140, 90, fill="red", width=3)
cnv.create_rectangle(50,20,140,80, fill="blue")

root.mainloop()


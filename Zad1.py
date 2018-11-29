import tkinter as tk
from tkinter import font as tkf

root = tk.Tk()
default_font = tkf.nametofont("TkDefaultFont")
default_font.configure(size=56)
root.option_add("*Font", default_font)

button = tk.Button(root, text="Nice Click!", command=lambda: print("Nice Click!"))
button.grid(column=0, row=1, sticky=tk.W)

var = tk.IntVar()
tk.Radiobutton(root, text="Red", value=1, variable=var, command=lambda: button.config(fg="red")).grid(column=0, row=2)
tk.Radiobutton(root, text="Yellow", value=2, variable=var, command=lambda: button.config(fg="yellow")).grid(column=0, row=3)
tk.Radiobutton(root, text="Green", value=3, variable=var, command=lambda: button.config(fg="green")).grid(column=0, row=4)

root.mainloop()

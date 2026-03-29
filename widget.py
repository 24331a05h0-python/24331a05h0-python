import tkinter as tk

root = tk.Tk()
root.title("Menu Example")

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

mb = tk.Menubutton(root, text="Options")
mb.pack()

mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1")
mb.menu.add_command(label="Option 2")

root.mainloop()

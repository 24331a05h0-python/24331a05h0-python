import tkinter as tk

root = tk.Tk()
root.title("Listbox and Scrollbar Example")

scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, yscrollcommand=scroll.set)

items = ["Python","Java","C","C++","HTML","CSS","JavaScript","SQL","PHP","Ruby"]

for item in items:
    listbox.insert(tk.END, item)

listbox.pack()

scroll.config(command=listbox.yview)

root.mainloop()

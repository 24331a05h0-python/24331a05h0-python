import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")

def show_text():
    name = entry.get()
    label2.config(text="Hello " + name)

label1 = tk.Label(root, text="Enter your name:")
label1.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=show_text)
button.pack()

label2 = tk.Label(root, text="")
label2.pack()

root.mainloop()

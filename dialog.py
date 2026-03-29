import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title("Messagebox and File Dialog Example")

def show_message():
    messagebox.showinfo("Message", "Hello! This is a Messagebox")

def open_file():
    file = filedialog.askopenfilename()
    messagebox.showinfo("Selected File", file)

button1 = tk.Button(root, text="Show Message", command=show_message)
button1.pack()

button2 = tk.Button(root, text="Open File", command=open_file)
button2.pack()

root.mainloop()

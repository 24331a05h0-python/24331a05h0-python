import tkinter as tk

root = tk.Tk()
root.title("CheckButton and Radiobutton Example")

var1 = tk.IntVar()
var2 = tk.IntVar()
course = tk.StringVar()

check1 = tk.Checkbutton(root, text="Python", variable=var1)
check1.pack()

check2 = tk.Checkbutton(root, text="Java", variable=var2)
check2.pack()

radio1 = tk.Radiobutton(root, text="Male", variable=course, value="Male")
radio1.pack()

radio2 = tk.Radiobutton(root, text="Female", variable=course, value="Female")
radio2.pack()

root.mainloop()

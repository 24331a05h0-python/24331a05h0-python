import tkinter as tk

root = tk.Tk()
root.title("Geometry Methods Example")
root.geometry("300x200")

label1 = tk.Label(root, text="Using Pack")
label1.pack()

label2 = tk.Label(root, text="Using Grid")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="Using Place")
label3.place(x=100, y=100)

root.mainloop()

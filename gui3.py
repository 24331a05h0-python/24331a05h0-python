import tkinter as tk

root = tk.Tk()
root.title("Geometry Methods Example")
root.geometry("300x200")

frame1 = tk.Frame(root)
frame1.pack()

label1 = tk.Label(frame1, text="Using Pack")
label1.pack()

frame2 = tk.Frame(root)
frame2.pack()

label2 = tk.Label(frame2, text="Using Grid")
label2.grid(row=0, column=0)

label3 = tk.Label(root, text="Using Place")
label3.place(x=100, y=120)

root.mainloop()

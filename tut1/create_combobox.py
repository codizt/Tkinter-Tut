import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox")
root.geometry("500x250")

ttk.Label(root, text="Months", background="green", foreground="white",
          font=("Times New Roman", 15)).grid(row=0, column=1)
ttk.Label(root, text="Select Month:", font=("Times New Roman", 10)
          ).grid(column=0, row=5, padx=10, pady=25)

n = tk.StringVar()
monthchoosen = ttk.Combobox(root, width=27, textvariable=n)

monthchoosen["values"] = ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                          'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
monthchoosen.grid(column=1, row=5)
monthchoosen.current(1)

root.mainloop()

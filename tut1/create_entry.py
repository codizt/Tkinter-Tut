from tkinter import *

root = Tk()
root.title("Entry Widget")
root.geometry("600x400")

name_var = StringVar()
pswd_var = StringVar()


def submit():
    name = name_var.get()
    pswd = pswd_var.get()

    print(f"The name is {name}.")
    print(f"The pasword is {pswd}")

    name_var.set("")
    pswd_var.set("")


name_label = Label(root, text="Username", font=(
    "calibre", 10, "bold")).grid(row=0, column=0)
name_entry = Entry(root, textvariable=name_var, font=(
    "calibre", 10, "normal")).grid(row=0, column=1)

pswd_label = Label(root, text="Password", font=(
    "calibre", 10, "bold")).grid(row=1, column=0)
pswd_entry = Entry(root, textvariable=pswd_var, font=(
    "calibre", 10, "normal")).grid(row=1, column=1)

sub_btn = Button(root, text="Submit", command=submit).grid(row=2, column=1)

root.mainloop()

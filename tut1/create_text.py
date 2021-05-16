from tkinter import *

root = Tk()
root.geometry("250x170")

T = Text(root, height=5, width=52)

l = Label(root, text="Fact of the day")
l.config(font=("Courier", 14))

Fact = """A man can be arrested for wearing a skirt in Public in Italy."""

b1 = Button(root, text="Next")
b2 = Button(root, text="Exit", command=root.destroy)

T.pack()
l.pack()
b1.pack()
b2.pack()

root.mainloop()

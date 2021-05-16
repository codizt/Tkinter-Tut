from tkinter import *

top = Tk()
top.geometry('450x300')

username = Label(top, text="Username").place(x=40, y=60)
password = Label(top, text="Password").place(x=40, y=100)
submit = Button(top, text="Submit").place(x=40, y=130)

name_input_area = Entry(top, width=30).place(x=110, y=60)
password_input_area = Entry(top, width=30).place(x=110, y=100)

top.mainloop()

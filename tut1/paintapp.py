from tkinter import *

root = Tk()

root.title = "Paint App"
root.geometry("500x350")


def display(event):
    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x+3), (event.y + 3)

    color = "green"

    w.create_line(x1, y1, x2, y2, fill=color)


w = Canvas(root, width=400, height=250)

w.bind("<B1-Motion>", display)

l = Label(root, text="Double Click and drag to draw.")
l.pack()
w.pack()

root.mainloop()

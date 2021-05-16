from tkinter import *
from tkinter.ttk import *

master = Tk()

v = StringVar(master, "1")

style = Style(master)
style.configure("TRadiobutton", background="light green",
                foreground="red", font=("arial", 10, "bold"))

radiobuttons = {"RadioButton 1": "1",
                "RadioButton 2": "2", "RadioButton 3": "3", "RadioButton 4": "4"}

for (name, value) in radiobuttons.items():
    Radiobutton(master, text=name, variable=v,
                value=value).pack(side=TOP, ipady=5)

master.mainloop()

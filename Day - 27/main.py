from tkinter import *


def button_clicked():
    x = text_input.get()
    my_label.config(text=x)


window = Tk()
window.title("Understanding - algo")
window.minsize(width=500, height=300)

# labels

my_label = Label(text="I'm keshav kaushik")
my_label.grid(column=0, row=0)

# my_label["text"] = "New Text"
# my_label.config(text="Sex")

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# new_button
button2 = Button(text="New_button")
button2.grid(column=2, row=0)

# Entry
text_input = Entry(width=15)
text_input.grid(column=3, row=2)

window.mainloop()

from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=130, height=100)
window.config(padx=10, pady=10)


def miles_to_km():
    km = int(int(my_input.get()) * 1.609)
    my_label3.config(text=str(km))


# entry
my_input = Entry()
my_input.grid(column=1, row=0)

# text
my_label = Label(text="Miles")
my_label.grid(column=3, row=0)

# Text 2
my_label2 = Label(text=f"is equal to")
my_label2.grid(column=0, row=1)

# text3
my_label3 = Label(text="0")
my_label3.grid(column=1, row=1)

# text 4
my_label4 = Label(text="KM")
my_label4.grid(column=2, row=1)

# button
button = Button(text="calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()
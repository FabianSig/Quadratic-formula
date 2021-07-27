from tkinter import *
from math import sqrt

def button_action():
    try:
        a = float(aEingabe.get())
        b = float(bEingabe.get())
        c = float(cEingabe.get())
    except ValueError:
        y = "ungültige Eingabe!"
        ausgabe.configure(text=y)

    try:
        x1 = ((-b+sqrt(b*b-4*a*c))/2*a)
        x2 = ((-b-sqrt(b*b-4*a*c))/2*a)
        y = "x1 = " + str(x1) + "\nx2 = " + str(x2)
        ausgabe.configure(text=y)
    except ValueError:
        y = "Keine Lösung"
        ausgabe.configure(text=y)

fenster = Tk()
fenster.title("Siggi\'s quadratischer Rechner")

aEingabe = Entry(fenster)
bEingabe = Entry(fenster)
cEingabe = Entry(fenster)
aEingabe.grid(row=1, column=1)
bEingabe.grid(row=2, column=1)
cEingabe.grid(row=3, column=1)

Label(text="a = ").grid(row=1)
Label(text="b = ").grid(row=2)
Label(text="c = ").grid(row=3)

Button(fenster, text="Berechnen!", font=("Helvetica", 16), command=button_action).grid(row=4)

ausgabe = Label(fenster, text=" ")
ausgabe.grid(row=5)
fenster.mainloop()

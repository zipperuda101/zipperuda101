import tkinter as tk
from tkinter import *
from functools import partial
win = Tk()
Label(win, text="First Number:", font=("Arial", 12), bg="#D80073").place(x=50, y=50)
num1 = Entry(win, width=15, font=("Arial", 14), bd=3)
num1.place(x=180, y=50)
Label(win, text="Second Number:", font=("Arial", 12), bg="#D80073").place(x=50, y=100)
num2 = Entry(win, width=15, font=("Arial", 14), bd=3)
num2.place(x=180, y=100)
result_text = Label(win, text="Result:", font=("Arial", 12), bg="#D80073")
result_text.place(x=50, y=150)
result_label = Label(win, text="00", font=("Arial", 14), bg="white", fg="blue", width=15, bd=3)
result_label.place(x=180, y=150)
def calculate(choice):
    try:
        n1, n2 = float(num1.get()), float(num2.get())
        if choice == "+": result, result_text['text'] = n1 + n2, "Sum:"
        elif choice == "-": result, result_text['text'] = n1 - n2, "Difference:"
        elif choice == "*": result, result_text['text'] = n1 * n2, "Product:"
        elif choice == "/": result, result_text['text'] = n1 / n2, "Quotient:"
        elif choice == "//": result, result_text['text'] = n1 // n2, "Floor Quotient:"
        elif choice == "^": result, result_text['text'] = n1 ** n2, "Power:"
        elif choice == "%": result, result_text['text'] = n1 % n2, "Remainder:"
        result_label.config(text=f"{result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input.")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by 0")
operations = [("+", 50), ("-", 130), ("*", 210), ("/", 290), ("//", 370), ("^", 450), ("%", 530)]
for (op, x) in operations:
    Button(win, text=op, font=("Arial", 18), width=4, command=partial(calculate, op)).place(x=x, y=220)
win.title("Python GUI: Basic Calculator v1")
win.geometry("625x300+650+320")
win.config(bg="#D80073")
win.mainloop()

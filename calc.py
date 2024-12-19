import tkinter as tk
from functools import partial
win = tk.Tk()
def panksyon(ma):
    current_text = res.cget("text")
    if current_text == "0" and ma not in ('C', '=', '0', '.'): current_text = ""
    if ma == 'C': res.config(text="0") 
    elif ma == '=':
            expression = current_text
            result = round(eval(expression), 2) 
            res.config(text=str(result))  
    else: res.config(text=current_text + ma)
res = tk.Label(win, text="0", width=25, font=('Arial', 24), justify='right', anchor='e', bd=12, relief="sunken")
res.grid(row=0, column=0, columnspan=4, pady=(20, 10))
btn_txt = [('**', '//', '%', 'C'), ('7', '8', '9', '+'), ('4', '5', '6', '-'), ('1', '2', '3', '/'), ('.', '0', '=', '*')]
for r, row in enumerate(btn_txt, 1):
    for i, text in enumerate(row):
        button = tk.Button(win, text=text, width=8, height=2, font=('Arial', 18), command=partial(panksyon, text))
        button.grid(row=r, column=i, padx=5, pady=5)
win.title("Calculator ni Zenia")
win.config(bg="#D80073")
win.geometry("528x525+650+270")
win.mainloop()

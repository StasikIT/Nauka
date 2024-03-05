import tkinter as tk
import tkinter.messagebox as msg
import math

def button_click(symbol):
    current = entry.get()
    if symbol == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Помилка!")
    elif symbol == 'C':
        entry.delete(0, tk.END)
    elif symbol == 'Вихід':
        if msg.askokcancel("Підтвердження", "Ви впевнені, що хочете вийти?"):
            root.quit()
    elif symbol == 'sin':
        try:
            result = math.sin(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Помилка!")
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    '1', '2', '3', '+', '*',
    '4', '5', '6', '-', '/',
    '7', '8', '9', '=', 'sin',
    '0', '.', 'C', 'Вихід'
]

row_index = 1
col_index = 0

for button in buttons:
    if button == 'Вихід':
        tk.Button(root, text=button, width=5, command=lambda b=button: button_click(b)).grid(row=row_index, column=col_index)
    else:
        tk.Button(root, text=button, width=5, command=lambda b=button: button_click(b)).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        col_index = 0
        row_index += 1

root.mainloop()

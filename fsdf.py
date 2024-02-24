import tkinter as tk
from tkinter import messagebox
import random

def submit():
    global d
    value1 = int(entry1.get())
    value2 = int(entry2.get())
    guessed_number_str = entry3.get()

    if guessed_number_str.isdigit():
        guessed_number = int(guessed_number_str)
        if value1 >= value2:
            messagebox.showerror("Помилка", "Перше значення не може бути більшим або рівним за друге.")
            d += 1
        else:
            random_value = int(root.title().split(": ")[-1])
            if guessed_number == random_value:
                messagebox.showinfo("Вітаємо!", "Ви вгадали число!")
            else:
                messagebox.showerror("Неправильно", f"Вибачте, правильне число було: {random_value}")
                d += 1

            if d == 5:
                messagebox.showinfo("Кінець гри", "Ви набрали 5 помилок. Гра завершена.")
                root.quit()
    else:
        messagebox.showerror("Помилка", "Введено нечислове значення для вгадування.")

def generate_random():
    value1 = int(entry1.get())
    value2 = int(entry2.get())
    random_value = random.randint(value1, value2)
    entry3.delete(0, tk.END)
    root.title(f'Згенероване число: {random_value}')
    change_button_color(generate_button)

def change_button_color(button):
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    button.config(bg=random_color)

def on_click_submit():
    submit()
    change_button_color(submit_button)

root = tk.Tk()
root.title('Вгадай число')
d = 0

label1 = tk.Label(root, text="Введіть значення 1:")
label1.configure(bg="light blue")
label1.pack()
entry1 = tk.Entry(root, validate="key")
entry1.pack()

label2 = tk.Label(root, text="Введіть значення 2:")
label2.configure(bg="light blue")
label2.pack()
entry2 = tk.Entry(root, validate="key")
entry2.pack()

generate_button = tk.Button(root, text="Згенерувати", command=generate_random)
generate_button.pack()

label3 = tk.Label(root, text="Вгадайте число:")
label3.configure(bg="light blue")
label3.pack()
entry3 = tk.Entry(root, validate="key")
entry3.pack()

submit_button = tk.Button(root, text="Спробувати", command=on_click_submit)
submit_button.pack()

root.configure(bg="light blue")
root.geometry("400x250")
root.mainloop()

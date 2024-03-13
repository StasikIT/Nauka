import tkinter as tk
from tkinter import messagebox as mb
import random

current_user = None
current_balance = 0
usd_balance = 0


def update_rate():
    global usd_to_uah_rate, usd_to_cny_rate
    usd_to_uah_rate = random.uniform(26, 28)
    usd_to_cny_rate = random.uniform(6, 7)
    root.title(f"Поточний курс: 1 Долар = {usd_to_uah_rate:.2f} гривень, 1 Долар = {usd_to_cny_rate:.2f} юанів")


def refill():
    refill_window = tk.Toplevel(root)
    refill_window.title("Поповнення")

    amount_label = tk.Label(refill_window, text="Сума:")
    amount_label.grid(row=0, column=0, padx=5, pady=5)

    amount_entry = tk.Entry(refill_window)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    card_label = tk.Label(refill_window, text="Номер картки:")
    card_label.grid(row=1, column=0, padx=5, pady=5)

    card_entry = tk.Entry(refill_window)
    card_entry.grid(row=1, column=1, padx=5, pady=5)
    card_entry.config(validate="key", validatecommand=(root.register(check_card_number), "%S"))

    confirm_button = tk.Button(refill_window, text="Підтвердити",
                               command=lambda: refill_confirm(amount_entry.get(), card_entry.get()))
    confirm_button.grid(row=2, columnspan=2, padx=5, pady=5)

def check_card_number(char):
    return char.isdigit() or char == ''

def refill_confirm(amount, card_number):
    global current_balance
    try:
        amount = float(amount)
        if amount <= 0:
            mb.showerror("Помилка", "Сума має бути більше нуля")
            return
        if len(card_number) != 8:
            mb.showerror("Помилка", "Номер картки має містити 8 цифр")
            return
        current_balance += amount
        mb.showinfo("Поповнення", f"Баланс поповнено на {amount} грн. Поточний баланс: {current_balance} грн.")
    except ValueError:
        mb.showerror("Помилка", "Неправильний формат введеної суми")

def check_input_char(char):
    return char.isdigit() or char == '.'

def show_password():
    if password_show_var.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

def authorize():
    global current_user
    username = username_entry.get()
    password = password_entry.get()
    if len(password) < 4 or len(password) > 8:
        show_error("Помилка", "Пароль має містити від 4 до 8 символів")
        return
    current_user = username
    root.deiconify()
    login_window.destroy()
    update_rate()


def view_password():
    password = password_entry.get()
    if password:
        mb.showinfo("Пароль", f"Ваш пароль: {password}")
    else:
        show_error("Помилка", "Пароль не введено")

def show_error(title, message):
    mb.showerror(title, message)


def show_warning(title, message):
    mb.showwarning(title, message)


def usd_to_uah(amount, rate):
    return amount * rate

def uah_to_usd(amount, rate):
    return amount /rate

def usd_to_cny(amount, rate):
    return amount * rate


def convert():
    amount = entry_amount.get()
    try:
        amount = float(amount)
        choice = option_menu_var.get()
        if choice == 'З Долара в Гривні':
            converted_amount = usd_to_uah(amount, usd_to_uah_rate)
            label_result.config(text=f"{amount} USD = {converted_amount:.2f} UAH")
        elif choice == 'З Гривні в Долар':
            converted_amount = uah_to_usd(amount, usd_to_uah_rate)
            label_result.config(text=f"{amount} UAH = {converted_amount:.2f} USD")
        elif choice == 'З Долара в Юани':
            converted_amount = usd_to_cny(amount, usd_to_cny_rate)
            label_result.config(text=f"{amount} USD = {converted_amount:.2f} CNY")
    except ValueError:
        label_result.config(
            text="Будь ласка, введіть число")
def show_profile():
    if current_user:
        profile_window = tk.Toplevel(root)
        profile_window.title("Мій кабінет")
        profile_window.geometry("200x100")

        profile_label = tk.Label(profile_window, text=f"Користувач: {current_user}\nБаланс: {current_balance} грн.")
        profile_label.pack(padx=5, pady=5)

        buy_usd_button = tk.Button(profile_window, text="Купити долари", command=buy_usd)
        buy_usd_button.pack(padx=5, pady=5)
    else:
        mb.showerror("Помилка", "Ви не авторизовані")

def buy_usd():
    global current_balance, usd_balance
    buy_usd_window = tk.Toplevel(root)
    buy_usd_window.title("Купівля доларів")
    buy_usd_window.geometry("200x100")

    amount_label = tk.Label(buy_usd_window, text="Сума:")
    amount_label.grid(row=0, column=0, padx=5, pady=5)

    amount_entry = tk.Entry(buy_usd_window)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    confirm_button = tk.Button(buy_usd_window, text="Підтвердити", command=lambda: buy_usd_confirm(amount_entry.get()))
    confirm_button.grid(row=1, columnspan=2, padx=5, pady=5)


def buy_usd_confirm(amount):
    global current_balance, usd_balance
    try:
        amount = float(amount)
        if amount <= 0:
            mb.showerror("Помилка", "Сума має бути більше нуля")
            return
        if current_balance < amount:
            mb.showerror("Помилка", "Недостатньо коштів на балансі")
            return
        current_balance -= amount
        usd_balance += amount
        mb.showinfo("Купівля доларів", f"Куплено {amount} USD. Поточний баланс: {current_balance} грн.")
    except ValueError:
        mb.showerror("Помилка", "Неправильний формат введеної суми")


login_window = tk.Tk()
login_window.title("Авторизація")
login_window.geometry("300x200")
username_label = tk.Label(login_window, text="Ім'я:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(login_window, text="Пароль:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(login_window, show='*')
password_entry.grid(row=1, column=1, padx=5, pady=5)

password_show_var = tk.BooleanVar()
password_show_checkbox = tk.Checkbutton(login_window, text="Показати пароль", variable=password_show_var,
                                        command=show_password)
password_show_checkbox.grid(row=2, columnspan=2, padx=5, pady=5)

login_button = tk.Button(login_window, text="Увійти", command=authorize)
login_button.grid(row=3, columnspan=2, padx=5, pady=5)

root = tk.Tk()
root.title("Конвертер валют")
root.withdraw()
label_amount = tk.Label(root, text="Введи число:")
label_amount.grid(row=1, column=0, padx=5, pady=5)

entry_amount = tk.Entry(root)
entry_amount.grid(row=1, column=1, padx=5, pady=5)
entry_amount.config(validate="key", validatecommand=(root.register(check_input_char), "%S"))

option_menu_var = tk.StringVar(root)
option_menu_var.set('З Долара в Гривні')
option_menu = tk.OptionMenu(root, option_menu_var, 'З Долара в Гривні', 'З Гривні в Долар', 'З Долара в Юани')
option_menu.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Порахувати", command=convert)
convert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

refill_button = tk.Button(root, text="Поповнити", command=refill)
refill_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

update_button = tk.Button(root, text="Оновити курс", command=update_rate)
update_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

profile_button = tk.Button(root, text="Мій кабінет", command=show_profile)
profile_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.geometry('400x300')
root.mainloop()

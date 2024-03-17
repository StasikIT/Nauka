import tkinter as tk
from tkinter import ttk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def buy_car():
    root.withdraw()  # Закриття головного вікна
    show_color_window()

def show_color_window():
    color_window = tk.Toplevel()
    color_window.title("Питання №2")

    window_width = 300
    window_height = 250
    center_window(color_window, window_width, window_height)

    selected_color = tk.StringVar()

    color_dict = {'зелений': 'green', 'червоний': 'red', 'синій': 'blue', 'жовтий': 'yellow', 'помаранчевий': 'orange', 'фіолетовий': 'purple', 'рожевий': 'pink', 'коричневий': 'brown', 'чорний': 'black', 'білий': 'white'}

    colors = list(color_dict.keys())
    color_combobox = ttk.Combobox(color_window, values=colors)
    color_combobox.set("Вибір кольору")
    color_combobox.pack(pady=10)

    def change_color():
        selected_color.set(color_dict[color_combobox.get()])
        color_square.config(bg=color_dict[color_combobox.get()])

    change_button = tk.Button(color_window, text="Помалювати", command=change_color)
    change_button.pack(pady=5)

    color_square = tk.Label(color_window, width=20, height=5, bg="white")
    color_square.pack(pady=10)

    def next_window():
        color_window.destroy()
        show_search_window()

    next_button = tk.Button(color_window, text="Далі", command=next_window)
    next_button.pack(pady=5)

def show_search_window():
    search_window = tk.Toplevel()
    search_window.title("Питання №3")
    center_window(search_window, 250, 350)

    label = ttk.Label(search_window, text="Введіть текст для пошуку:")
    label.pack(pady=5)

    entry = ttk.Entry(search_window)
    entry.pack(pady=5)

    def search(event=None):
        search_text = entry.get().lower()
        car_listbox.delete(0, tk.END)
        count = 0
        for car in cars:
            if search_text in car.lower():
                car_listbox.insert(tk.END, car)
                count += 1
            if count >= 4:
                break

    entry.bind("<KeyRelease>", search)

    car_listbox = tk.Listbox(search_window)
    car_listbox.pack(pady=5)

    def next_window():
        search_window.destroy()
        show_next_question_window()

    next_button = tk.Button(search_window, text="Далі", command=next_window)
    next_button.pack(pady=5)

def show_next_question_window():
    next_window = tk.Toplevel()
    next_window.title("Питання №4")
    center_window(next_window, 250, 150)

    var = tk.IntVar()

    def show_selected_volume():
        selected_volume = var.get()
        if selected_volume == 1:
            print("Об'єм двигуна: до 1200")
        elif selected_volume == 2:
            print("Об'єм двигуна: від 1200 до 1500")
        elif selected_volume == 3:
            print("Об'єм двигуна: від 1500 до 2500")
        elif selected_volume == 4:
            print("Об'єм двигуна: більше 2500")

        next_window.destroy() # Закриваємо вікно після натискання кнопки "Далі"
        show_question5_window()

    tk.Radiobutton(next_window, text="До 1200", variable=var, value=1, command=show_selected_volume).pack(anchor=tk.W)
    tk.Radiobutton(next_window, text="Від 1200 до 1500", variable=var, value=2, command=show_selected_volume).pack(anchor=tk.W)
    tk.Radiobutton(next_window, text="Від 1500 до 2500", variable=var, value=3, command=show_selected_volume).pack(anchor=tk.W)
    tk.Radiobutton(next_window, text="Більше 2500", variable=var, value=4, command=show_selected_volume).pack(anchor=tk.W)

def show_question5_window():
    question_window5 = tk.Toplevel()
    question_window5.title("Питання №5")
    center_window(question_window5, 250, 150)

    engine_var = tk.StringVar()

    tk.Label(question_window5, text="Вид мотору:").pack()

    tk.Radiobutton(question_window5, text="Бензин", variable=engine_var, value="Бензин").pack(anchor=tk.W)
    tk.Radiobutton(question_window5, text="Дизель", variable=engine_var, value="Дизель").pack(anchor=tk.W)

    def next_window():
        selected_engine = engine_var.get()
        question_window5.destroy()  # Закриття поточного вікна

        characteristics_window = tk.Toplevel()  # Створення нового вікна для характеристик
        characteristics_window.title("Характеристики авто")
        center_window(characteristics_window, 300, 150) # Центрування вікна

        # Передача даних для відображення у вікні характеристик авто
        car_name = ""  # Назва авто, введена користувачем у попередніх питаннях
        engine_volume = ""  # Об'єм двигуна, введений користувачем у попередніх питаннях
        car_condition = ""  # Стан авто, введений користувачем у попередніх питаннях

        # Відображення характеристик авто
        tk.Label(characteristics_window, text=f"Назва авто: {car_name}").pack()
        tk.Label(characteristics_window, text=f"Вид мотору: {selected_engine}").pack()
        tk.Label(characteristics_window, text=f"Об'єм двигуна: {engine_volume}").pack()
        tk.Label(characteristics_window, text=f"Машина: {car_condition}").pack()

        def close_characteristics_window():
            characteristics_window.destroy()

        tk.Button(characteristics_window, text="Закрити", command=close_characteristics_window).pack(pady=5)

    next_button = tk.Button(question_window5, text="Підтвердити", command=next_window)
    next_button.pack(pady=10)

# Статичний список автомобілів
cars = ["BMW", "Audi", "Mercedes", "Ford", "Toyota", "Lexus", "Chevrolet", "Subaru", "Volkswagen"]

# Створюємо головне вікно
root = tk.Tk()
root.title('Питання №1')

car_choice = tk.IntVar()

tk.Label(root, text="Оберіть тип автомобіля:").pack()

tk.Radiobutton(root, text="Новий", variable=car_choice, value=1).pack()
tk.Radiobutton(root, text="Старий", variable=car_choice, value=2).pack()

tk.Button(root, text="Далі", command=buy_car).pack()
center_window(root, 250, 150)

root.mainloop()

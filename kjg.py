import tkinter as tk
from tkinter import ttk

questions = [
    {
        'question': 'Що таке Патон?',
        'answers': ['Мова програмування', 'Елементарна частичка', 'Металургічна печь', 'Історична постать'],
        'correct_answer': 0
    },
    {
        'question': 'Який рік створення мови Патон?',
        'answers': ['1998', '2005', '1987', '1977'],
        'correct_answer': 3
    },
    {
        'question': 'Хто є творцем мови Патон?',
        'answers': ['Іван Патон', 'Михайло Патон', 'Павло Патон', 'Василь Патон'],
        'correct_answer': 0
    },
    {
        'question': 'Для чого призначена мова програмування Патон?',
        'answers': ['Для масштабних обчислень', 'Для веб-розробки', 'Для мобільних додатків', 'Для наукових досліджень'],
        'correct_answer': 0
    },
    {
        'question': 'Яка типізація мови Патон?',
        'answers': ['Статична', 'Динамічна', 'Слабо типізована', 'Сильно типізована'],
        'correct_answer': 3
    },
    {
        'question': 'Чим відрізняється мова Патон від інших мов програмування?',
        'answers': ['Вона має особливий синтаксис', 'Вона спеціалізована для обчислень з великими обсягами даних',
                    'Вона проста у використанні', 'Вона має багато вбудованих бібліотек'],
        'correct_answer': 1
    },
    {
        'question': 'Які переваги має мова програмування Патон?',
        'answers': ['Велика швидкодія', 'Простота синтаксису', 'Підтримка багатопоточності', 'Велика кількість фреймворків'],
        'correct_answer': 2
    },
    {
        'question': 'Які недоліки має мова програмування Патон?',
        'answers': ['Мале співтовариство розробників', 'Низька ефективність', 'Складність у вивченні',
                    'Обмежена функціональність'],
        'correct_answer': 0
    },
    {
        'question': 'Яка парадигма програмування притаманна мові Патон?',
        'answers': ['Об’єктно-орієнтоване програмування', 'Процедурне програмування', 'Функціональне програмування',
                    'Логічне програмування'],
        'correct_answer': 1
    },
    {
        'question': 'Який файловий розширення використовується для програм на мові Патон?',
        'answers': ['.pat', '.py', '.ptn', '.pato'],
        'correct_answer': 2
    },
    {
        'question': 'Що виводить функція print() у мові програмування Патон?',
        'answers': ['Текст', 'Графіки', 'Числа', 'Рядки'],
        'correct_answer': 3
    },
    {
        'question': 'Яка функція використовується для введення даних з клавіатури в мові Патон?',
        'answers': ['read()', 'input()', 'get_input()', 'accept()'],
        'correct_answer': 1
    }
]

def show_score():
    score_window = tk.Toplevel(root)
    score_window.title("Результат")
    score_window.configure(background='black')
    ttk.Label(score_window, text=f"Привіт, {username.get()}! Ви набрали {score.get()} балів.",
              foreground='green').pack(padx=20, pady=10)


def next_question(question_number):
    if question_number < len(questions):
        question_window = ttk.Frame(tab_control)
        tab_control.add(question_window, text=f"Питання {question_number + 1}")
        tab_control.pack(expand=1, fill="both")

        question_text = questions[question_number]['question']
        question_label = ttk.Label(question_window, text=question_text, foreground='green')
        question_label.pack(padx=20, pady=10)

        for i, answer in enumerate(questions[question_number]['answers']):
            answer_radio = ttk.Radiobutton(question_window, text=answer, variable=selected_answer,
                                           value=i, style='Wild.TRadiobutton')
            answer_radio.pack(padx=20, pady=5)

        next_button = ttk.Button(question_window, text="Далі", command=lambda: process_answer(question_number))
        next_button.pack(pady=10)
    else:
        show_score()
        root.quit()


def process_answer(question_number):
    selected_index = selected_answer.get()
    if selected_index == questions[question_number]['correct_answer']:
        score.set(score.get() + 1)
    tab_control.hide(tab_control.select())
    next_question(question_number + 1)


def start_test():
    root.withdraw()  # Приховати головне вікно
    new_window = tk.Toplevel()  # Створити нове вікно
    new_window.configure(background='black')  # Задати фон для нового вікна

    global tab_control
    tab_control = ttk.Notebook(new_window)

    next_question(0)  # Почати тест


# Головне вікно
root = tk.Tk()
root.title("Введіть ім'я")
root.configure(background='black')

username = tk.StringVar()
score = tk.IntVar()
selected_answer = tk.IntVar()

username_label = ttk.Label(root, text="Введіть своє ім'я:", foreground='green').pack(pady=10)
username_entry = ttk.Entry(root, textvariable=username).pack(pady=5)
start_button = ttk.Button(root, text="Почати тест", command=start_test).pack(pady=10)

# Стилізація радіокнопок
style = ttk.Style()
style.configure('Wild.TRadiobutton', foreground='orange')

root.mainloop()


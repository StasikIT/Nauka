from tkinter import *

def insert_text():
    input_text = root.clipboard_get()
    entry.insert("insert", input_text)

def clear_text():
    entry.delete("sel.first", "sel.last")

def copy_text():
    input_text = entry.selection_get()
    root.clipboard_clear()
    root.clipboard_append(input_text)

def align_left():
    entry.tag_configure("align", justify='left')
    entry.tag_add("align", "1.0", "end")

def align_center():
    entry.tag_configure("align", justify='center')
    entry.tag_add("align", "1.0", "end")

def align_right():
    entry.tag_configure("align", justify='right')
    entry.tag_add("align", "1.0", "end")

root = Tk()

entry = Text(root, width=50, height=5, font=('Arial', 12), bg="light blue")
entry.grid(row=0, column=0, columnspan=3, pady=10)

button_insert = Button(root, text="Вставити", command=insert_text, bg="light yellow")
button_insert.grid(row=1, column=0, padx=5)

button_clear = Button(root, text="Стерти текст", command=clear_text, bg="light yellow")
button_clear.grid(row=1, column=1, padx=5)

button_copy = Button(root, text="Копіювати текст", command=copy_text, bg="light yellow")
button_copy.grid(row=1, column=2, padx=5)

button_align_left = Button(root, text="Ліво", command=align_left, bg="light yellow")
button_align_left.grid(row=2, column=0, padx=5)

button_align_center = Button(root, text="Центр", command=align_center, bg="light yellow")
button_align_center.grid(row=2, column=1, padx=5)

button_align_right = Button(root, text="Право", command=align_right, bg="light yellow")
button_align_right.grid(row=2, column=2, padx=5)

result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, pady=10)

root.geometry("450x200")
root.mainloop()

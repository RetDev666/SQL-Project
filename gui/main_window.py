# gui/main_window.py
import tkinter as tk
from tkinter import ttk
from db.queries import get_materials

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Складські матеріали")

        # Таблиця матеріалів
        self.tree = ttk.Treeview(root, columns=("ID", "Назва", "Одиниця", "Мінімум", "Дата закінчення"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Назва", text="Назва")
        self.tree.heading("Одиниця", text="Одиниця")
        self.tree.heading("Мінімум", text="Мінімум")
        self.tree.heading("Дата закінчення", text="Дата закінчення")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Кнопка для оновлення даних
        self.load_data_button = tk.Button(root, text="Завантажити дані", command=self.load_data)
        self.load_data_button.pack(pady=5)

        self.load_data()

    def load_data(self):
        # Очищення таблиці
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Завантаження даних
        materials = get_materials()
        for material in materials:
            self.tree.insert("", "end", values=material)

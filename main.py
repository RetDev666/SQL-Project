from PyQt5 import QtWidgets
import sys
from db.queries import get_materials  # Імпорт функцій для роботи з базою даних

# Імпортуємо відповідні класи для підвікон
from gui.add_material import AddMaterialWindow
from gui.move_material import MoveMaterialWindow
from gui.issue_material import IssueMaterialWindow

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Складські матеріали")
        self.setGeometry(100, 100, 500, 400)
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        # Кнопка для перегляду матеріалів
        view_materials_button = QtWidgets.QPushButton("Перегляд матеріалів")
        view_materials_button.clicked.connect(self.view_materials)
        layout.addWidget(view_materials_button)

        # Кнопка для додавання нового матеріалу
        add_material_button = QtWidgets.QPushButton("Додати матеріал")
        add_material_button.clicked.connect(self.open_add_material_window)
        layout.addWidget(add_material_button)

        # Кнопка для переміщення матеріалу
        move_material_button = QtWidgets.QPushButton("Перемістити матеріал")
        move_material_button.clicked.connect(self.open_move_material_window)
        layout.addWidget(move_material_button)

        # Кнопка для видачі матеріалу
        issue_material_button = QtWidgets.QPushButton("Видати матеріал")
        issue_material_button.clicked.connect(self.open_issue_material_window)
        layout.addWidget(issue_material_button)

        self.setLayout(layout)

    def view_materials(self):
        materials = get_materials()

        if not materials:
            QtWidgets.QMessageBox.information(self, "Інформація", "Немає матеріалів для відображення.")
            return

        # Створюємо нове вікно для відображення матеріалів
        view_window = QtWidgets.QWidget()
        view_window.setWindowTitle("Список матеріалів")
        layout = QtWidgets.QVBoxLayout()

        # Додаємо кожен матеріал у вигляді рядка в QLabel
        for material in materials:
            # Представляємо кожен матеріал у вигляді форматованого рядка
            material_info = f"ID: {material[0]}, Назва: {material[1]}, Одиниця: {material[2]}, Мінімальний запас: {material[3]}, Термін придатності: {material[4]}"
            layout.addWidget(QtWidgets.QLabel(material_info))

        view_window.setLayout(layout)
        view_window.setGeometry(150, 150, 500, 400)
        view_window.show()
        self.view_window = view_window  # Зберігаємо посилання, щоб уникнути автоматичного закриття

    def open_add_material_window(self):
        self.add_window = AddMaterialWindow()  # Створюємо екземпляр без аргументів
        self.add_window.show()

    def open_move_material_window(self):
        self.move_window = MoveMaterialWindow()  # Створюємо екземпляр без аргументів
        self.move_window.show()

    def open_issue_material_window(self):
        self.issue_window = IssueMaterialWindow()  # Створюємо екземпляр без аргументів
        self.issue_window.show()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

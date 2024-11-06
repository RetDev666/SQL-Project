from PyQt5 import QtWidgets
from db.queries import add_material
from PyQt5.QtWidgets import QMessageBox

class AddMaterialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Додати матеріал")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QFormLayout()

        self.name_entry = QtWidgets.QLineEdit()
        self.unit_entry = QtWidgets.QLineEdit()
        self.min_stock_level_entry = QtWidgets.QLineEdit()
        self.expiration_date_entry = QtWidgets.QLineEdit()

        layout.addRow("Назва матеріалу:", self.name_entry)
        layout.addRow("Одиниця вимірювання:", self.unit_entry)
        layout.addRow("Мінімальний запас:", self.min_stock_level_entry)
        layout.addRow("Термін придатності (YYYY-MM-DD):", self.expiration_date_entry)

        add_button = QtWidgets.QPushButton("Додати")
        add_button.clicked.connect(self.add_material)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_material(self):
        name = self.name_entry.text()
        unit = self.unit_entry.text()
        min_stock_level_text = self.min_stock_level_entry.text()
        expiration_date = self.expiration_date_entry.text()

        if not min_stock_level_text.isdigit():
            QMessageBox.critical(self, "Помилка", "Мінімальний запас має бути цілим числом.")
            return

        min_stock_level = int(min_stock_level_text)
        add_material(name, unit, min_stock_level, expiration_date)
        self.close()

from PyQt5 import QtWidgets
from db.queries import move_material
from PyQt5.QtWidgets import QMessageBox

class MoveMaterialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перемістити матеріал")
        self.setGeometry(100, 100, 400, 250)
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QFormLayout()

        self.material_id_entry = QtWidgets.QLineEdit()
        self.from_location_entry = QtWidgets.QLineEdit()
        self.to_location_entry = QtWidgets.QLineEdit()
        self.quantity_entry = QtWidgets.QLineEdit()

        layout.addRow("ID матеріалу:", self.material_id_entry)
        layout.addRow("Початкове місце:", self.from_location_entry)
        layout.addRow("Кінцеве місце:", self.to_location_entry)
        layout.addRow("Кількість:", self.quantity_entry)

        move_button = QtWidgets.QPushButton("Перемістити")
        move_button.clicked.connect(self.move_material)
        layout.addWidget(move_button)

        self.setLayout(layout)

    def move_material(self):
        material_id_text = self.material_id_entry.text()
        from_location = self.from_location_entry.text()
        to_location = self.to_location_entry.text()
        quantity_text = self.quantity_entry.text()

        if not material_id_text.isdigit() or not quantity_text.isdigit():
            QMessageBox.critical(self, "Помилка", "ID матеріалу та кількість мають бути цілими числами.")
            return

        material_id = int(material_id_text)
        quantity = int(quantity_text)

        move_material(material_id, from_location, to_location, quantity)
        self.close()

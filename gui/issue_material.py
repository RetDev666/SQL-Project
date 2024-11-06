from PyQt5 import QtWidgets
from db.queries import issue_material
from PyQt5.QtWidgets import QMessageBox

class IssueMaterialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Видати матеріал")
        self.setGeometry(100, 100, 400, 250)
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QFormLayout()

        self.material_id_entry = QtWidgets.QLineEdit()
        self.quantity_entry = QtWidgets.QLineEdit()
        self.issued_to_entry = QtWidgets.QLineEdit()
        self.purpose_entry = QtWidgets.QLineEdit()

        layout.addRow("ID матеріалу:", self.material_id_entry)
        layout.addRow("Кількість:", self.quantity_entry)
        layout.addRow("Отримувач:", self.issued_to_entry)
        layout.addRow("Ціль використання:", self.purpose_entry)

        issue_button = QtWidgets.QPushButton("Видати")
        issue_button.clicked.connect(self.issue_material)
        layout.addWidget(issue_button)

        self.setLayout(layout)

    def issue_material(self):
        material_id_text = self.material_id_entry.text()
        quantity_text = self.quantity_entry.text()
        issued_to = self.issued_to_entry.text()
        purpose = self.purpose_entry.text()

        if not material_id_text.isdigit() or not quantity_text.isdigit():
            QMessageBox.critical(self, "Помилка", "ID матеріалу та кількість мають бути цілими числами.")
            return

        material_id = int(material_id_text)
        quantity = int(quantity_text)

        issue_material(material_id, quantity, issued_to, purpose)
        self.close()

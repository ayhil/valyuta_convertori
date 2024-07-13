from PySide6.QtWidgets import QApplication
from asosiy import widget

app = QApplication()

window = widget()
window.show()

app.exec()
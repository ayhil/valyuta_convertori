from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget,QMessageBox
from convertor_iu import Ui_Form

class widget(QWidget,Ui_Form):

    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.valyuta = 12665
        self.lineEdit.clear()
        self.pushButton.clicked.connect(self.clear)
        self.lineEdit.textChanged.connect(self.usd)

    def usd(self):
        if self.lineEdit.text() and self.lineEdit.text().isdigit():
            qiymat = int(self.lineEdit.text())
            qiymat = round(qiymat / self.valyuta,2)

            self.lineEdit_2.setText(str(qiymat))

    def clear(self):
        savol = QMessageBox.question(None,"savol","Siz programani yopmoqchimisiz",
                                                  QMessageBox.Yes | QMessageBox.No)

        if savol == QMessageBox.Yes:
            self.close()

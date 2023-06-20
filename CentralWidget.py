from PyQt6.QtWidgets import QWidget,   QLabel , QGridLayout, QPushButton, QLineEdit, QApplication, QMessageBox
from PyQt6.QtCore import pyqtSlot


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)


        self.label=QLabel("nutzername eingebn",self)
        self.label1=QLabel("paswort angeben", self)
        self.button_login=QPushButton("login", self)
        self.button_login.clicked.connect(self.einlogen)
        self.button_cancel=QPushButton("cancel", self)

        self.button_cancel.clicked.connect(QApplication.instance().quit)
        self.passwort=QLineEdit(self)
        self.nutzername=QLineEdit(self)
        self.passwort.setEchoMode(QLineEdit.EchoMode.Password)


        layout = QGridLayout(self)
        layout.addWidget(self.label1, 1, 1)
        layout.addWidget(self.label, 2, 1)
        layout.addWidget(self.button_login, 3,1)
        layout.addWidget(self.button_cancel, 3, 3)
        layout.addWidget(self.passwort, 1, 2)
        layout.addWidget(self.nutzername, 2, 2)


    def einlogen(self):
        if self.passwort.text() =="12345" and self.nutzername.text() =="freddy":
            QMessageBox.information(self, "Ergebnis", "Erfolgreicher login") , QApplication.instance().quit()
        else:
            print("faile")


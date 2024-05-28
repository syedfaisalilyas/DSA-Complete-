import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess
import queue as q

# int<q> q1
# int<q> q2
# int<q> q3
# int<q> q4

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("test.ui", self)

        self.Submit.clicked.connect(self.run_script)

    def run_script(self):
        pass
        # q1.add(self.name.textedit.entereddata)
        # q2.add(self.gender.textedit.entereddata)
        # q4.add(self.age.textedit.entereddata)
        # q3.add(self.cnic.textedit.entereddata)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("adminMainUI.ui", self)

        # Connect each button to its corresponding function
        self.addUser.clicked.connect(self.run_addUser_script)
        self.graphs.clicked.connect(self.run_graphs_script)
        self.serachFlights.clicked.connect(self.run_searching_script)

    def run_addUser_script(self):
        script_path = "AddRemoveUser/Add_Remove_User.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")

    def run_graphs_script(self):
        script_path = "Graphs/graph.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")

    def run_searching_script(self):
        script_path = "Trees/multiLevelSearching.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

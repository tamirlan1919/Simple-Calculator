import sys

from kalc import *
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec())
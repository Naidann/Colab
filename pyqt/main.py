from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
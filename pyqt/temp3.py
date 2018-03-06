from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt5.QtGui import QIcon

a = QApplication(sys.argv)


jan = QMainWindow()
jan.setGeometry(50, 50, 250, 300)
jan.setWindowTitle("Janela teste QMainWindow")
jan.setWindowIcon(QIcon("teste.jpg"))
jan.statusBar().showMessage("Mensagem")

b = QPushButton("Olá Mundo", jan)
b.move(100, 100)
b.clicked.connect(QApplication.instance().quit)


jan.show()

sys.exit(a.exec_())
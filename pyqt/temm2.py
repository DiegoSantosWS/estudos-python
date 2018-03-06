from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

a = QApplication(sys.argv)


jan = QWidget()
jan.resize(400, 300)
jan.setWindowTitle("Janela teste widget")
jan.move(500, 50)
b = QPushButton("Olá Mundo", jan)
b.move(100, 100)
b.clicked.connect(QApplication.instance().quit)


jan.show()

sys.exit(a.exec_())
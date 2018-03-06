from PyQt5.QtWidgets import QApplication, QDialog
import sys

a = QApplication(sys.argv)
print("Argumentos: ", sys.argv)

jan = QDialog()

jan.show()

sys.exit(a.exec_())
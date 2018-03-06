from PyQt5.QtWidgets import (QApplication, QGridLayout, 
                             QLabel, QLineEdit, QWidget)

class ExemploGridLayout(QWidget):
    def __init__(self):
        super(ExemploGridLayout, self).__init__()
        self.setWindowTitle("Exemplo QGrideLayout")
        self.addComponentes()
        self.definirLayput()

    def addComponentes(self):
        self.label = QLabel("Label")
        self.edit = QLineEdit()

        self.label2 = QLabel("Label 2")
        self.edit2 = QLineEdit()

        self.label3 = QLabel("Label 3")
        self.edit3 = QLineEdit()

    def definirLayput(self):
        layout_jan = QGridLayout()
        layout_jan.addWidget(self.label, 0, 0)
        layout_jan.addWidget(self.edit, 1, 0)

        layout_jan.addWidget(self.label2, 0, 1)
        layout_jan.addWidget(self.edit2, 1, 1)

        layout_jan.addWidget(self.label3, 2, 0)
        layout_jan.addWidget(self.edit3, 3, 0, 1, 2)
        self.setLayout(layout_jan)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    jan = ExemploGridLayout()
    jan.show()
    sys.exit(app.exec_())
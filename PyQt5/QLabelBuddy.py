#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
QLabel与伙伴控制

mainLayout.addWidget(控件对象, rowIndex, columnIndex， row， column)

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置伙伴控制')
        self.setWindowIcon(QIcon('image.ico'))
        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)

        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)

        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QLabelBuddy()
    main.show()

    sys.exit(app.exec_())

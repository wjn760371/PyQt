#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

QLineEdit控件与回显模式

EchoMode(回显模式)

4种回显模式

1、Normal
2、NoEcho 如输入已提交到计算机，但不在屏幕上显示
3、Password 主要用于输入密码
4、PasswordEchoOnEdit 如一些输入密码显示一小段时间后变为*

'''

from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formlayout = QFormLayout() # 表单布局

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formlayout.addRow("Normal", normalLineEdit)
        formlayout.addRow("NoEcho", noEchoLineEdit)
        formlayout.addRow("Password", passwordLineEdit)
        formlayout.addRow("PasswordEchoOnEdit", passwordEchoOnEditLineEdit)

        # placeholdertext

        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('Password')
        passwordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoOnEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QLineEditEchoMode()
    main.show()

    sys.exit(app.exec_())

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget

def onClinc_button():
    print('1')
    print('widger.x() = %d' % widget.x()) # 250  （窗口横坐标）
    print('widger.y() = %d' % widget.y()) # 200  （窗口纵坐标）
    print('widger.width() = %d' % widget.width()) # 300  （工作区宽度）
    print('widger.height() = %d' % widget.height()) # 240  （工作区高度）

    print('2')
    print('widger.geometry().x() = %d' % widget.geometry().x()) # 250  （工作区横坐标）
    print('widger.geometry().y() = %d' % widget.geometry().y()) # 222  （工作区纵坐标）
    print('widger.geometry().width() = %d' % widget.geometry().width()) # 300  （工作区宽度）
    print('widger.geometry().height() = %d' % widget.geometry().height()) # 240  （工作区高度）

    print('3')
    print('widger.frameGeometry().x() = %d' % widget.frameGeometry().x()) # 250  （窗口横坐标）
    print('widger.frameGeometry().y() = %d' % widget.frameGeometry().y()) # 200  （窗口纵坐标）
    print('widger.frameGeometry().width() = %d' % widget.frameGeometry().width()) # 316  （窗口宽度）
    print('widger.frameGeometry().height() = %d' % widget.frameGeometry().height()) # 278  （窗口高度）


app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClinc_button)

btn.move(24,52)

widget.resize(300,240)     # 设置工作区的尺寸

widget.move(250,200)

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())
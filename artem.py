from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*


#створення додатка
app=QApplication([])
win=QWidget()

win.resize(500,500)
win.setWindowTitle('Тест ГітХаб')

title=QLabel('Тестовий додаток для гібХаб')

line_h=QHBoxLayout()
line_h.addWidget(title)

win.setLayout(line_h)

win.show()
app.exec_()

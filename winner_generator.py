from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout
from random import randint

app = QApplication([])
wind = QWidget()


wind.setWindowTitle('Определитель победителя')
wind.move(100,100)
wind.resize(500,200)

text = QLabel('Нажми,чтобы узнать победителя')
winner = QLabel('?')
button = QPushButton('Сгенерировать')

vline = QVBoxLayout()

vline.addWidget(text,alignment=Qt.AlignCenter)
vline.addWidget(winner,alignment=Qt.AlignCenter)
vline.addWidget(button,alignment=Qt.AlignCenter)

wind.setLayout(vline)

def show_winner():
    text.setText('Победитель:')
    winner.setText(  str(randint(1,100))  )

button.clicked.connect(show_winner)


wind.show()
app.exec_()
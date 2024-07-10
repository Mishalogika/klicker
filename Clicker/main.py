#pip instal pyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

lbl = QLabel("Кликер (●'◡'●)")
btn = QPushButton("Тапай!")

main_layout = QVBoxLayout()
main_layout.addWidget(lbl)
main_layout.addWidget(btn)

window.setLayout(main_layout)
window.show()
app.exec()
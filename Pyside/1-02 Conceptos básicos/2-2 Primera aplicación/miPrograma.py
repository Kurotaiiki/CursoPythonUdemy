from importlib import import_module
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow  
import sys

app=QApplication(sys.argv)
window= QMainWindow()
window.setWindowTitle("Hola mundo")
boton=QPushButton("Soy un boton")

window.setCentralWidget(boton)

window.show()
sys.exit(app.exec())
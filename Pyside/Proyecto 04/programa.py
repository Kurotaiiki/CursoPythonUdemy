from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenu, QListWidgetItem, QInputDialog)
from PySide6.QtCore import Qt, QEvent
from ui_kanban import Ui_MainWindow
from helpers import *
import csv

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.listas=[self.lista_Pendientes,self.lista_EnProgreso,self.lista_Completadas]

        for lista in self.listas:
            lista.clear()
            lista.installEventFilter(self)
            lista.itemDoubleClicked.connect(self.actualizarTarea)

        if existsFile(absPath("tareas.csv")):
            with open(absPath("tareas.csv"),newline="\n") as csvfile:
                reader=csv.reader(csvfile,delimiter=",")
                for lista,nombre in reader:
                    item=QListWidgetItem(nombre)
                    item.setTextAlignment(Qt.AlignCenter)
                    self.listas[int(lista)].addItem(item)

    def eventFilter(self,source,event):
        if (event.type()==QEvent.ContextMenu):
            menu=QMenu()
            menu.addAction("Crear tarea",self.crearTarea)

            item=source.itemAt(event.pos())
            menu.addAction("Borrar tarea",lambda: self.borrarTarea(item))
            menu.addAction("Debuggear tarea",lambda: self.Debugear_tarea(item))

            if menu.exec_(event.globalPos()):
                return True
        return super().eventFilter(source,event)

    def Debugear_tarea(self,item):
        if isinstance(item,QListWidgetItem):
            print(item.text())
        print("Debugeando Tarea")

    def borrarTarea(self,item):
        if isinstance(item,QListWidgetItem):
            itemIndex=item.listWidget().row(item)
            item.listWidget().takeItem(itemIndex)

    def actualizarTarea(self,item):
        lista=item.listWidget()
        itemIndex=lista.row(item)
        lista.takeItem(itemIndex)

        if  (self.listas.index(lista)) < len(self.listas)-1 :
            lista=self.listas[(self.listas.index(lista))+1].addItem(item)                
  
    def crearTarea(self):
        tarea,_=QInputDialog.getText(self,"Tareas","Nombre de la tarea?")
        if tarea:
            item= QListWidgetItem(tarea)
            item.setTextAlignment(Qt.AlignCenter)
            self.lista_Pendientes.addItem(item)

    def closeEvent(self, event):
        tareas=[]
        for i,lista in enumerate(self.listas):
            for j in range(lista.count()):
                tareas.append([i,lista.item(j).text()])

        with open(absPath("tareas.csv"),"w",newline="\n") as csvfile:
            writer =csv.writer(csvfile,delimiter=',')
            writer.writerows(tareas)
        event.accept()        

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()

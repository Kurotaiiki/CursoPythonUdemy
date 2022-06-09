from enum import auto
from symtable import Symbol
from PySide6 import QtWidgets
from ui_monitor import Ui_MainWindow
from functools import partial
import pyqtgraph as pg  # pip install pyqtgraph
import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sondas=[
            {'nombre':'Sonda 1','valores':[],'color':'r','symbolo':'o'},
            {'nombre':'Sonda 2','valores':[],'color':'b','symbolo':'+'},
            {'nombre':'Sonda 3','valores':[],'color':'g','symbolo':'star'},        
        ]

        

        self.valores=[10,12,14,16,15,13,11,9]
        self.valores2=[1,2,4,6,5,3,1,-3]


        self.construirGrafico()

        self.pushButton.clicked.connect(self.nuevaLectura)
        self.pushButton_2.clicked.connect(partial( self.nuevaLectura,True))


    def construirGrafico(self):
        self.widget.addLegend()
        self.widget.setBackground('w')

        # self.widget.plot(self.valores,pen=pg.mkPen('b', width=3 ),name='sonda 1',symbol='o',symbolBrush='b',symbolsize=12)
        # self.widget.plot(self.valores2,pen=pg.mkPen('r', width=3 ),name='sonda 2',symbol='+',symbolBrush='r',symbolsize=14)
        self.graficos=[]
        for sonda in self.sondas:
            self.comboBox.addItem(sonda['nombre'])
            plot=self.widget.plot(sonda['valores'],name=sonda['nombre'],
                             pen=pg.mkPen(sonda['color'], width=3 ),
                             symbol=sonda['symbolo'],
                             symbolBrush=sonda['color'],symbolsize=20)
            self.graficos.append(plot)

        

        self.widget.showGrid(x=True,y=True)
        # self.widget.setXRange(0,10)
        self.widget.setYRange(-20,30)
        self.widget.setTitle('Monitor de temperaturas',size='24px')
        styles={'color':'#000','font-size':'20px'}
        self.widget.setLabel('left','Temperatura (C)',**styles)
        self.widget.setLabel('bottom','Tiempo (H)',**styles)
    
    def nuevaLectura(self, autogenerar = False):
        if not autogenerar:
            indice=self.comboBox.currentIndex()
            temperatura=self.spinBox.value()

            self.sondas[indice]['valores'].append(temperatura)
            self.graficos[indice].setData(self.sondas[indice]['valores'])
        else:
            for indice,sonda in enumerate(self.sondas):
                temperatura=random.randint(-20,30)
                sonda['valores'].append(temperatura)
                self.graficos[indice].setData(sonda['valores'])


  






if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()

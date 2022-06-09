import sys
from tkinter import SEL_LAST
from PySide6 import QtCore, QtGui, QtWidgets
from functools import partial
from helpers import absPath
from cartas import *


class Jugador:
    def __init__(self,nombre):
        self.mano = []
        self.nombre = nombre
        self.puntos=0
        self.plantado=False

    def sumar(self,carta):
        self.mano.append(carta)
        self.calcular()

    def calcular(self):
        self.puntos=0
        #sumar normales y visibles 
        for carta in self.mano:
            if carta.visible:
                if carta.nombre not in ['As','Jota','Reina','Rey']:
                    self.puntos += carta.numero
                elif carta.nombre in ['Jota','Reina','Rey']:
                    self.puntos += 10
        # sumamos AS visibles
        for carta in self.mano:
            if carta.visible:
                if carta.nombre == 'As':
                    #sumamos 1 u 11 segun si nos pasamos o no 
                    if self.puntos+ 11 <= 21:
                        self.puntos +=11
                    else:
                        self.puntos +=1
    
    def consultar(self):
        print(f"{self.nombre}: {[f'{c.nombre} de {c.palo}' for c in self.mano if c.visible]} ({self.puntos})")


class BlackJack:
    def __init__(self,baraja):
        self.baraja=baraja
        self.humano = Jugador('Felipe')
        self.banca = Jugador('Banca')


    def repartir(self,jugador,voltear=True):
        carta=self.baraja.extraer()
        if carta:
            if voltear:
                carta.mostrar()
            #dar carta a jugador
            jugador.sumar(carta)
        return carta

    def ganador(self):
        # 0 empate   1 humano  2 banca
        if self.humano.puntos >21:
            return 2
        if self.banca.puntos >21:
            return 1
        if self.humano.puntos > self.banca.puntos:
            return 1
        elif self.humano.puntos < self.banca.puntos:
            return 2
        else:
            return 0

    def comprobarGanador(self):
        ganador = self.ganador()
        if ganador == 2 :
            print('gana la banca')
        elif ganador == 1 : 
            print('gana el humano')
        else:
            print('empate')

    def reiniciar(self):
        self.baraja.reiniciar()
        self.humano = Jugador('Felipe')
        self.banca = Jugador('Banca')



            
        
            

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuramos la ventana y el fondo
        self.setWindowTitle("Blackjack sin apuestas")
        self.setFixedSize(900, 630)
        # Configuración de la baraja
        self.baraja = Baraja(self)
        self.setCentralWidget(self.baraja)
        #crear blackJack
        self.bj = BlackJack(self.baraja)
        # Interfaz (después de asignar el widget central para sobreponerla)
        self.setupUi()
        # Posicionamos las cartas y hacemos el reparto inicial
        self.preparar()
        # Creamos las señales
        self.btnPedir.clicked.connect(self.pedir)
        self.btnPlantar.clicked.connect(self.plantar)
        self.btnReiniciar.clicked.connect(self.reiniciar)

        self.finalizado = False



    def preparar(self):
        """ Posiciona la baraja inicial y ejecuta los primeros repartos"""
        self.registro.append(f"== Empieza Blackjack ==")
        offset = 0
        for carta in self.baraja.cartas:
            carta.posicionar(45 + offset, 205 + offset)
            offset += 0.25
        #activar botones
        self.btnPedir.setEnabled(True)
        self.btnPlantar.setEnabled(True)
        self.btnReiniciar.setEnabled(True)
        self.repartirUI(self.bj.humano)
        self.repartirUI(self.bj.humano)
        self.repartirUI(self.bj.banca)
        self.repartirUI(self.bj.banca,False)

    def repartirUI(self, jugador, voltear=True):
        carta = self.bj.repartir(jugador,voltear)
        if jugador == self.bj.humano:
            offset_x = len(self.bj.humano.mano) * 40
            carta.mover(195 + offset_x, 320 , duracion = 750)
        elif jugador == self.bj.banca:
            offset_x = len(self.bj.banca.mano) * 25
            carta.mover(251 + offset_x, 110 , duracion = 750, escalado = 0.8)
        self.marcadores()

    
            


    def pedir(self):
        """ Desactiva los botones de la interfaz y pide una carta """
        self.btnPedir.setEnabled(False)
        self.btnPlantar.setEnabled(False)
        self.btnReiniciar.setEnabled(False)
        self.repartirUI(self.bj.humano)
        self.comprobar()

    def comprobar(self):
        self.btnReiniciar.setEnabled(True)
        #comprobar puntos humano
        if self.bj.humano.puntos < 21:
            self.btnPedir.setEnabled(True)
            self.btnPlantar.setEnabled(True)
        else:
            self.bj.humano.plantado=True
            #movimiento de la banca
            self.jugarBanca()

    def plantar(self):
        """ Planta al usuario e inicia la jugada de la banca """
        self.btnPedir.setEnabled(False)
        self.btnPlantar.setEnabled(False)
        self.bj.humano.plantado = True
        #movimiento de la banca
        self.jugarBanca()

    def jugarBanca(self):
        if self.bj.humano.puntos > 21 :
             self.bj.banca.plantado = True
        else:
        #     #voltamos la carta de la banca
            if len(self.bj.banca.mano) == 2 :
                self.bj.banca.mano[-1].mostrar()
                self.bj.banca.calcular()
                self.marcadores()
        #     # si tiene mas de 17
            if self.bj.banca.puntos >= 17 or self.bj.banca.puntos > self.bj.humano.puntos:
                self.bj.banca.plantado = True
            if not self.bj.banca.plantado:
                self.repartirUI(self.bj.banca)
                self.jugarBanca()
    
        self.ganador()



    def reiniciar(self):
        """ Reinicia los marcadores, el registro y prepara un nuevo juego """
        self.finalizado = False
        self.marcadorJugador.setText("0")
        self.marcadorBanca.setText("0")
        self.registro.setText("")
        self.bj.reiniciar()
        self.preparar()

    def marcadores(self):
        self.marcadorJugador.setText(f"{self.bj.humano.puntos}")
        self.marcadorBanca.setText(f"{self.bj.banca.puntos}")
        self.registro.append(f'{self.bj.humano.nombre}[{self.bj.humano.puntos}]\t,{self.bj.banca.nombre}[{self.bj.banca.puntos}]')
        self.registro.verticalScrollBar().setValue(self.registro.verticalScrollBar().maximum())

    def setupUi(self):
        self.setStyleSheet("""
            QTextEdit {background-color: #ddd; font-size:13px }
            QLabel { color: white; font-size: 40px; font-weight: 500 }
            QPushButton { background-color: #20581e; color: white;font-size: 15px }
            QPushButton:disabled { background-color: #163914 }""")
        # Configuración del fondo
        tablero = QtGui.QImage(absPath("images/Tablero.png"))
        paleta = QtGui.QPalette()
        paleta.setBrush(QtGui.QPalette.Window, QtGui.QBrush(tablero))
        self.setPalette(paleta)
        # Marcadores
        self.marcadorBanca = QtWidgets.QLabel("0", self)
        self.marcadorBanca.resize(50, 50)
        self.marcadorBanca.move(342, 19)
        self.marcadorJugador = QtWidgets.QLabel("0", self)
        self.marcadorJugador.resize(50, 50)
        self.marcadorJugador.move(355, 557)
        # Botones
        self.btnPedir = QtWidgets.QPushButton("Pedir carta", self)
        self.btnPedir.resize(175, 32)
        self.btnPedir.move(692, 495)
        self.btnPlantar = QtWidgets.QPushButton("Plantarse", self)
        self.btnPlantar.resize(175, 32)
        self.btnPlantar.move(692, 535)
        self.btnReiniciar = QtWidgets.QPushButton("Reiniciar", self)
        self.btnReiniciar.resize(175, 32)
        self.btnReiniciar.move(692, 575)
        # Texto para el registro
        self.registro = QtWidgets.QTextEdit(self)
        self.registro.setReadOnly(True)
        self.registro.move(692, 285)
        self.registro.resize(175, 185)

    def ganador(self):
        if self.bj.humano.plantado and self.bj.banca.plantado and not self.finalizado:
            if self.bj.ganador()== 2 :
                self.registro.append(f'== Ganador {self.bj.banca.nombre} ==')
            elif self.bj.ganador()== 1 :
                self.registro.append(f'== Ganador {self.bj.humano.nombre} ==')
            else :
                self.registro.append(f'=== Es un empate ===')
            self.registro.verticalScrollBar().setValue(self.registro.verticalScrollBar().maximum())
            self.finalizado = True


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # exec_() si PySide6 < 6.1.0 (pip install --upgrade pyside6)
    sys.exit(app.exec())


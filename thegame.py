from graphics import *
import tkinter as tk
def main():
    win = GraphWin('Game', 800,900)
    #win.setCoords(0,0,)
    logo = Image(Point(399,150),"IMG_0082.gif")
    logo.draw(win)
    
    
    rec = Rectangle(Point(100,100), Point(300,300))
    rec.draw(win)
    
       



    win.getMouse()
    win.close()

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput 
        break 

def movimiento(board, jugada, turno, columnas, filas, i):
    board[columnas-i][jugada-1] = turno
    
    ''' if board[columnas-i][jugada-1] == 0:
        board[columnas-2][jugada-1] = turno
    else:
        while board[columnas-2][jugada-1] != 0:
            newcolumnas = columnas - 2
            columnas = newcolumnas - 1
        board[columnas][jugada-1] = turno '''
    


def validacion_entradas(jugada, jugador):
    while True:
        try:
            while True:
                jugada = int(input(jugador +" entre el numero de la columna que desea jugar (1-7): "))
                
                return  jugada
        except ValueError:
            print('El valor entrado no es valido. Vuelva a intentarlo.')
            continue
        else:
            return  jugada
        break

def proximo_espacio_disponible(board, jugada, turno, columnas, filas):
    i = 2
    while True:
        try:
            while board[columnas-i][jugada-1] != 0:
                i = i + 1
            return i
        except ValueError:
            break
            


def columnaLlena():
    pass

def connect():
    #Variables
    columnas = 7
    filas = 6
    finJuego = False
    turno = 2
    jugada = 0

    #Board para el juego
    board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()

    #Entrada de turnos
    while finJuego == False:
        try:
            if turno == 2:
                jugador = "Jugador #1"
                jugada = validacion_entradas(jugada, jugador)
                while jugada < 1 or jugada > 7:
                    jugada = validacion_entradas(jugada, jugador)
                turno = 1
            else:
                jugador = "Jugador #2"
                jugada = validacion_entradas(jugada, jugador)
                turno = 2
        
        #entradas(turno)
            i = proximo_espacio_disponible(board,jugada,turno, columnas, filas)
        except ValueError:
            print('Columna llena. Intente otra columna.')
            continue

        movimiento(board,jugada,turno, columnas, filas, i)
        for row in board:
            for elem in row:
                print(elem, end=' ')
            print()
    

def entradas(turno):
    jugada = 0
    if turno == 2:
        jugador = "Jugador #1"
        jugada = validacion_entradas(jugada, jugador)
        while jugada < 1 or jugada > 7:
            jugada = validacion_entradas(jugada, jugador)
        turno = 1
    else:
        jugador = "Jugador #2"
        jugada = validacion_entradas(jugada, jugador)
        turno = 2


connect()
#main()
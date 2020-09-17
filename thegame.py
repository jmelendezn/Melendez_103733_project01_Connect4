from graphics import *
import tkinter as tk

# ----------------------------------------------Pantalla grafica----------------------------------------------
def main():
    win = GraphWin('Game', 800,900)
    win.setCoords(0,0,100,100)
    logo = Image(Point(22,83),"IMG_0082.gif")
    
    #Instrucciones
    rec = Rectangle(Point(45,92), Point(90,78))
    instrucciones = Text(rec.getCenter(), "Este espacio es para escribir\ncomo funciona este juego y las reglas.")

    #Linea divisoria
    div = Line(Point(10,68), Point(90,68))

    gameBoard = Rectangle(Point(13,60), Point(87,5))
    #Circulos 10.57  12.33

    c11 = Circle(Point(23.57,12.33),3)

    c21 = c11.clone()
    c21.move(10.57,0)

    c31 = c11.clone()
    c31.move(21.14,0)

    c41 = c11.clone()
    c41.move(21.14,0)
    
    #Draw
    logo.draw(win)
    instrucciones.draw(win)
    rec.draw(win)
    div.draw(win)

    c11.draw(win)
    c21.draw(win)
    c31.draw(win)
    c41.draw(win)
    c51.draw(win)
    c61.draw(win)
    c71.draw(win)
    c12.draw(win)
    c22.draw(win)
    c32.draw(win)
    gameBoard.draw(win)
    
       



    win.getMouse()
    win.close()


# ----------------------------------------------Juego no grafico----------------------------------------------
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

# ----------------------------------------------Se añade la pieza al board----------------------------------------------
def movimiento(board, jugada, turno, columnas, filas, i):
    board[columnas-i][jugada-1] = turno
    
    ''' if board[columnas-i][jugada-1] == 0:
        board[columnas-2][jugada-1] = turno
    else:
        while board[columnas-2][jugada-1] != 0:
            newcolumnas = columnas - 2
            columnas = newcolumnas - 1
        board[columnas][jugada-1] = turno '''
    

# ----------------------------------------------Se reciben los input de los jugadores y se valida que el mismo entre un numero entero----------------------------------------------
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

# ----------------------------------------------Determina cual es el proximo espacio disponible en cada columna----------------------------------------------
def proximo_espacio_disponible(board, jugada, turno, columnas, filas):
    i = 2
    while True:
        try:
            while board[columnas-i][jugada-1] != 0:
                i = i + 1
                if i > 7:
                    print('Esta columna ya esta llena. Intente en otra.')
                    i = 8
                    if turno == 1:
                        turno = 2
                    else:
                        turno = 1
                    break
            return i
        except ValueError:
            print('Esta columna ya esta llena. Intente en otra.')
            break
            
def entradas(turno, jugada):
    jugada = 0
    if turno == 2:
        jugador = "Jugador #1"
        jugada = validacion_entradas(jugada, jugador)
        while jugada < 1 or jugada > 7:
            jugada = validacion_entradas(jugada, jugador)
        turno = 1
        return jugada, turno 
    else:
        jugador = "Jugador #2"
        jugada = validacion_entradas(jugada, jugador)
        turno = 2
        return jugada, turno

def columnaLlena():
    pass

# ----------------------------------------------Codigo main (No utiliza graphic.py)----------------------------------------------
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
            ''' if turno == 2:
                jugador = "Jugador #1"
                jugada = validacion_entradas(jugada, jugador)
                while jugada < 1 or jugada > 7:
                    jugada = validacion_entradas(jugada, jugador)
                turno = 1
            else:
                jugador = "Jugador #2"
                jugada = validacion_entradas(jugada, jugador)
                turno = 2 '''
        
            jugada, turno = entradas(turno, jugada)
            i = proximo_espacio_disponible(board,jugada,turno, columnas, filas)
            while i == 8:
                if turno == 1:
                    turno = 2
                else:
                    turno = 1
                jugada, turno = entradas(turno, jugada)
                i = proximo_espacio_disponible(board,jugada,turno, columnas, filas)
        except ValueError:
            print('Columna llena. Intente otra columna.')
            continue

        movimiento(board,jugada,turno, columnas, filas, i)
        for row in board:
            for elem in row:
                print(elem, end=' ')
            print()
    
#connect()
main()
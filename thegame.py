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

# Se dibuja el area de juego
    gameBoard = Rectangle(Point(13,60), Point(87,5))
    gameBoard.setFill('blue')
    gameBoard.draw(win)
# Se dibujan todos los circulos
    mx = 10.57
    my = 12.33
    #Primera fila
    c11 = Circle(Point(8.57,11.5),3)
    c21 = c11.clone()
    c31 = c11.clone()
    c41 = c11.clone()
    c51 = c11.clone()
    c61 = c11.clone()
    c71 = c11.clone()
    #Segunda fila
    c12 = c11.clone()
    c22 = c11.clone()
    c32 = c11.clone()
    c42 = c11.clone()
    c52 = c11.clone()
    c62 = c11.clone()
    c72 = c11.clone()
    #Tercera fila
    c13 = c11.clone()
    c23 = c11.clone()
    c33 = c11.clone()
    c43 = c11.clone()
    c53 = c11.clone()
    c63 = c11.clone()
    c73 = c11.clone()
    #Cuarta fila
    c14 = c11.clone()
    c24 = c11.clone()
    c34 = c11.clone()
    c44 = c11.clone()
    c54 = c11.clone()
    c64 = c11.clone()
    c74 = c11.clone()
    #Quinta fila
    c15 = c11.clone()
    c25 = c11.clone()
    c35 = c11.clone()
    c45 = c11.clone()
    c55 = c11.clone()
    c65 = c11.clone()
    c75 = c11.clone()
    #Sexta fila
    c16 = c11.clone()
    c26 = c11.clone()
    c36 = c11.clone()
    c46 = c11.clone()
    c56 = c11.clone()
    c66 = c11.clone()
    c76 = c11.clone()

    #fila 1
    fila1 = [c11,c21,c31,c41,c51,c61,c71]
    for c in fila1:
        c.move(mx,0)
        c.setFill('white')
        c.draw(win)
        mx = mx + 10.2
    mx = 10.2
    my = 10.33
    #fila 2
    fila2 = [c12,c22,c32,c42,c52,c62,c72]
    for j in fila2:
        j.move(mx,8)
        j.setFill('white')
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 3
    fila3 = [c13,c23,c33,c43,c53,c63,c73]
    for j in fila3:
        j.move(mx,16)
        j.setFill('white')
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 4
    fila4 = [c14,c24,c34,c44,c54,c64,c74]
    for j in fila4:
        j.move(mx,24)
        j.setFill('white')
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    my = 10.33
    # Fila 5
    fila5 = [c15,c25,c35,c45,c55,c65,c75]
    for j in fila5:
        j.move(mx,32)
        j.setFill('white')
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 6
    fila6 = [c16,c26,c36,c46,c56,c66,c76]
    for j in fila6:
        j.move(mx,40)
        j.setFill('white')
        j.draw(win)
        mx = mx + 10.2

# Coneccion con juego no grafico
    k = win.getKey()
    
    

# Se dibujan mas
    logo.draw(win)
    instrucciones.draw(win)
    rec.draw(win)
    div.draw(win)

    
    
    
       



    win.getMouse()
    win.close()


# ----------------------------------------------Juego no grafico----------------------------------------------

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
    
connect()
#main()
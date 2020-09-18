from graphics import *
import tkinter as tk

# ----------------------------------------------Pantalla grafica----------------------------------------------
def main():
    win = GraphWin('Game', 800,900)
    win.setCoords(0,0,100,100)
    logo = Image(Point(22,83),"IMG_0082.gif")
    

#Texto de error
    errorTxt = Text(Point(49,62), ' ')
    errorTxt.setSize(13)
    errorTxt.setStyle('bold')
    errorTxt.setTextColor('red')
    errorTxt.draw(win)
#Instrucciones
    rec = Rectangle(Point(45,92), Point(90,78))
    instrucciones = Text(rec.getCenter(), "Conecta 4 fichas de forma horizontal, \nvertical o diagonal para ganar. \nEl primer jugador tendra fichas rojas \ny el segundo jugador tendra fichas amarrillas.")


#Linea divisoria
    div = Line(Point(10,68), Point(90,68))

# Se dibuja el area de juego
    gameBoard = Rectangle(Point(13,60), Point(87,5))
    gameBoard.setFill(color_rgb(37,68,65))
    gameBoard.draw(win)
    num1 = Text(Point(9,3), '1')
    num1.setSize(14)
    num1.setStyle('bold')
    # num1.draw(win) 
    num2 = num1.clone()
    num3 = num1.clone()
    num4 = num1.clone()
    num5 = num1.clone()
    num6 = num1.clone()
    num7 = num1.clone()
    
    j = 0
    mx = 10.2
    numeros = [num1, num2, num3, num4, num5, num6, num7]
    for i in numeros:
        i.move(mx,0)
        j = j+1
        i.setText(j)
        i.draw(win)
        mx = mx + 10.2
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
    for j in fila1:
        j.move(mx,0)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 2
    fila2 = [c12,c22,c32,c42,c52,c62,c72]
    for j in fila2:
        j.move(mx,8)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 3
    fila3 = [c13,c23,c33,c43,c53,c63,c73]
    for j in fila3:
        j.move(mx,16)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 4
    fila4 = [c14,c24,c34,c44,c54,c64,c74]
    for j in fila4:
        j.move(mx,24)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    my = 10.33
    # Fila 5
    fila5 = [c15,c25,c35,c45,c55,c65,c75]
    for j in fila5:
        j.move(mx,32)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 6
    fila6 = [c16,c26,c36,c46,c56,c66,c76]
    for j in fila6:
        j.move(mx,40)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2

# Se dibujan mas
    logo.draw(win)
    instrucciones.draw(win)
    rec.draw(win)
    div.draw(win)

    
# Coneccion con juego no grafico
    
    connect(win, fila1, fila2, fila3, fila4, fila5,fila6,errorTxt)
    
       



    win.getMouse()
    win.close()

def cambioColor(main):
    pass
    

# ----------------------------------------------Juego no grafico----------------------------------------------

# ----------------------------------------------Se añade la pieza al board----------------------------------------------
def movimiento(board, jugada, turno, columnas, filas, i, win,fila1, fila2, fila3, fila4, fila5,fila6):
    board[columnas-i][jugada-1] = turno
    print("\n",columnas-i, " ", jugada-1)
    if turno == 1:
        teamcolor = color_rgb(150,2,0) #Color rojo (Jugador1)
    else:
        teamcolor = color_rgb(245,203,92) #Color amarrillo (Jugador2)
    if columnas-i == 5 and jugada-1 == 0:   #Fila 1
        fila1[0].setFill(teamcolor) #11
        fila1[0].setOutline(teamcolor) 
    elif columnas-i == 5 and jugada-1 == 1:
        fila1[1].setFill(teamcolor) #12
        fila1[1].setOutline(teamcolor)
    elif columnas-i == 5 and jugada-1 == 2:
        fila1[2].setFill(teamcolor) #13
        fila1[2].setOutline(teamcolor)
    elif columnas-i == 5 and jugada-1 == 3:
        fila1[3].setFill(teamcolor) #14
        fila1[3].setOutline(teamcolor)
    elif columnas-i == 5 and jugada-1 == 4:
        fila1[4].setFill(teamcolor) #15
        fila1[4].setOutline(teamcolor)
    elif columnas-i == 5 and jugada-1 == 5:
        fila1[5].setFill(teamcolor) #16
        fila1[5].setOutline(teamcolor)
    elif columnas-i == 5 and jugada-1 == 6:
        fila1[6].setFill(teamcolor) #17
        fila1[6].setOutline(teamcolor)
    elif columnas-i == 4 and jugada-1 == 0: #FILA 2
        fila2[0].setFill(teamcolor)
        fila2[0].setOutline(teamcolor)
    elif columnas-i == 4 and jugada-1 == 1:
        fila2[1].setFill(teamcolor)
        fila2[1].setOutline(teamcolor)
    elif columnas-i == 4 and jugada-1 == 2:
        fila2[2].setFill(teamcolor)
        fila2[2].setOutline(teamcolor)
    elif columnas-i == 4 and jugada-1 == 3:
        fila2[3].setFill(teamcolor)
        fila2[3].setOutline(teamcolor)
    elif columnas-i == 4 and jugada-1 == 4:
        fila2[4].setFill(teamcolor)
        fila2[4].setOutline(teamcolor)
    elif columnas-i == 4 and jugada-1 == 5:
        fila2[5].setFill(teamcolor)
        fila2[5].setOutline(teamcolor)
    elif columnas-i == 4 and jugada-1 == 6:
        fila2[6].setFill(teamcolor)
        fila2[6].setOutline(teamcolor)
    elif columnas-i == 3 and jugada-1 == 0: #FILA 3
        fila3[0].setFill(teamcolor)
        fila3[0].setOutline(teamcolor)
    elif columnas-i == 3 and jugada-1 == 1:
        fila3[1].setFill(teamcolor)
        fila3[1].setOutline(teamcolor)
    elif columnas-i == 3 and jugada-1 == 2:
        fila3[2].setFill(teamcolor)
        fila3[2].setOutline(teamcolor)
    elif columnas-i == 3 and jugada-1 == 3:
        fila3[3].setFill(teamcolor)
        fila3[3].setOutline(teamcolor)
    elif columnas-i == 3 and jugada-1 == 4:
        fila3[4].setFill(teamcolor)
        fila3[4].setOutline(teamcolor)
    elif columnas-i == 3 and jugada-1 == 5:
        fila3[5].setFill(teamcolor)
        fila3[5].setOutline(teamcolor)
    elif columnas-i == 3 and jugada-1 == 6:
        fila3[6].setFill(teamcolor)
        fila3[6].setOutline(teamcolor)
    elif columnas-i == 2 and jugada-1 == 0: #FILA 4
        fila4[0].setFill(teamcolor)
        fila4[0].setOutline(teamcolor)
    elif columnas-i == 2 and jugada-1 == 1:
        fila4[1].setFill(teamcolor)
        fila4[1].setOutline(teamcolor)
    elif columnas-i == 2 and jugada-1 == 2:
        fila4[2].setFill(teamcolor)
        fila4[2].setOutline(teamcolor)
    elif columnas-i == 2 and jugada-1 == 3:
        fila4[3].setFill(teamcolor)
        fila4[3].setOutline(teamcolor)
    elif columnas-i == 2 and jugada-1 == 4:
        fila4[4].setFill(teamcolor)
        fila4[4].setOutline(teamcolor)
    elif columnas-i == 2 and jugada-1 == 5:
        fila4[5].setFill(teamcolor)
        fila4[5].setOutline(teamcolor)
    elif columnas-i == 2 and jugada-1 == 6:
        fila4[6].setFill(teamcolor)
        fila4[6].setOutline(teamcolor)
    elif columnas-i == 1 and jugada-1 == 0: #FILA 5
        fila5[0].setFill(teamcolor)
        fila5[0].setOutline(teamcolor)
    elif columnas-i == 1 and jugada-1 == 1:
        fila5[1].setFill(teamcolor)
        fila5[1].setOutline(teamcolor)
    elif columnas-i == 1 and jugada-1 == 2:
        fila5[2].setFill(teamcolor)
        fila5[2].setOutline(teamcolor)
    elif columnas-i == 1 and jugada-1 == 3:
        fila5[3].setFill(teamcolor)
        fila5[3].setOutline(teamcolor)
    elif columnas-i == 1 and jugada-1 == 4:
        fila5[4].setFill(teamcolor)
        fila5[4].setOutline(teamcolor)
    elif columnas-i == 1 and jugada-1 == 5:
        fila5[5].setFill(teamcolor)
        fila5[5].setOutline(teamcolor)
    elif columnas-i == 1 and jugada-1 == 6:
        fila5[6].setFill(teamcolor)
        fila5[6].setOutline(teamcolor)
    elif columnas-i == 0 and jugada-1 == 0: #FILA 6
        fila6[0].setFill(teamcolor)
        fila6[0].setOutline(teamcolor)
    elif columnas-i == 0 and jugada-1 == 1:
        fila6[1].setFill(teamcolor)
        fila6[1].setOutline(teamcolor)
    elif columnas-i == 0 and jugada-1 == 2:
        fila6[2].setFill(teamcolor)
        fila6[2].setOutline(teamcolor)
    elif columnas-i == 0 and jugada-1 == 3:
        fila6[3].setFill(teamcolor)
        fila6[3].setOutline(teamcolor)
    elif columnas-i == 0 and jugada-1 == 4:
        fila6[4].setFill(teamcolor)
        fila6[4].setOutline(teamcolor)
    elif columnas-i == 0 and jugada-1 == 5:
        fila6[5].setFill(teamcolor)
        fila6[5].setOutline(teamcolor)
    elif columnas-i == 0 and jugada-1 == 6:
        fila6[6].setFill(teamcolor)
        fila6[6].setOutline(teamcolor)



    

# ----------------------------------------------Se reciben los input de los jugadores y se valida que el mismo entre un numero entero----------------------------------------------
def validacion_entradas(jugada, jugador, win,errorTxt):
    while True:
        try:
            while True:
                textturno = Text(Point(49,65), jugador + ' entre el numero de la columna que desea ubicar su ficha')
                textturno.draw(win)
                jugada = int(win.getKey())
                textturno.setText(' ')
                errorTxt.setText(' ')
                return  jugada
        except ValueError:
            errorTxt.setText('El valor entrado no es valido. Vuelva a intentarlo.')
            textturno.setText(' ')
            continue
        else:
            return  jugada
        break

# ----------------------------------------------Determina cual es el proximo espacio disponible en cada columna----------------------------------------------
def proximo_espacio_disponible(board, jugada, turno, columnas, filas,errorTxt):
    i = 2
    while True:
        try:
            while board[columnas-i][jugada-1] != 0:
                i = i + 1
                if i > 7:
                    errorTxt.setText('Esta columna ya esta llena. Intente en otra.')
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
            
def entradas(turno, jugada, win,fila1, fila2, fila3, fila4, fila5,fila6,errorTxt):
    jugada = 0
    if turno == 2:
        jugador = "Jugador #1"
        jugada = validacion_entradas(jugada, jugador, win,errorTxt)
        if jugada < 1 or jugada > 7:
            errorTxt.setText('El valor entrado no es valido. Vuelva a intentarlo.')
            while jugada < 1 or jugada > 7:
                jugada = validacion_entradas(jugada, jugador,win,errorTxt)
        turno = 1
        return jugada, turno 
    else:
        jugador = "Jugador #2"
        jugada = validacion_entradas(jugada, jugador, win,errorTxt)
        if jugada < 1 or jugada > 7:
            errorTxt.setText('El valor entrado no es valido. Vuelva a intentarlo.')
            while jugada < 1 or jugada > 7:
                jugada = validacion_entradas(jugada, jugador,win,errorTxt)
        turno = 2
        return jugada, turno

def columnaLlena():
    pass

def verificar_ganador(board, jugada, turno):
    #Verificar horizontal
    for i in range(3):
            for j in range(6):
                if board[i][j] == turno and board[i+1][j] == turno and board[i+2][j] == turno and board[i+3][j] == turno:
                    return 4
    #Verificar vertical                                    
    for i in range(6):
            for j in range(3):
                if board[i][j] == turno and board[i][j+1] == turno and board[i][j+2] == turno and board[i][j+3] == turno:
                    return 4
    #Verificar diagonal hacia atras
    for i in range(3):
            for j in range(6):
                if board[i][j] == turno and board[i+1][j+1] == turno and board[i+2][j+2] == turno and board[i+3][j+3] == turno:
                    return 4
    #Verificar diagonal hacia adelante
    for i in range(6):
            for j in range(3):
                if board[i][j] == turno and board[i-1][j+1] == turno and board[i-2][j+2] == turno and board[i-3][j+3] == turno:
                    return 4
    return False

def pantalla_ganadora (win, ganador):
    rec2 = Rectangle(Point(21.5,40), Point(77,25))
    rec2.setFill(color_rgb(255,89,94))
    

    textoganador = Text(rec2.getCenter(), ganador + ' \nFelicidades has ganado')
    textoganador.setSize(20)
    textoganador.setTextColor('white')
    textoganador.setStyle('bold')

    textosalida = Text(Point(49,65), 'TOQUE LA PANTALLA PARA SALIR DEL JUEGO')
    textosalida.setSize(20)
    textosalida.setStyle('bold')

    objetos_ganadores = [rec2,textoganador,textosalida]
    for i in objetos_ganadores:
        i.draw(win)

# ----------------------------------------------Codigo main (No utiliza graphic.py)----------------------------------------------
def connect(win,fila1, fila2, fila3, fila4, fila5,fila6,errorTxt):
    #Variables
    columnas = 7
    filas = 6
    finJuego = 0
    turno = 2
    jugada = 0

    #Board para el juego
    board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()

    #Entrada de turnos
    while finJuego != 4:
      
        jugada, turno = entradas(turno, jugada, win,fila1, fila2, fila3, fila4, fila5,fila6,errorTxt)
        i = proximo_espacio_disponible(board,jugada,turno, columnas, filas,errorTxt)
        while i == 8:
            if turno == 1:
                turno = 2
            else:
                turno = 1
            jugada, turno = entradas(turno, jugada, win,fila1, fila2, fila3, fila4, fila5,fila6,errorTxt)
            i = proximo_espacio_disponible(board,jugada,turno, columnas, filas,errorTxt)
        

        movimiento(board,jugada,turno, columnas, filas, i, win,fila1, fila2, fila3, fila4, fila5,fila6)
        
        finJuego = verificar_ganador(board, jugada, turno)
        if turno == 1:
            ganador = 'Jugador #1'
        else:
            ganador = 'Jugador #2'
    pantalla_ganadora (win, ganador)
main()


            
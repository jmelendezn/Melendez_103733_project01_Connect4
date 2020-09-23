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
    c50 = Circle(Point(8.57,11.5),3)
    c51 = c50.clone()
    c52 = c50.clone()
    c53 = c50.clone()
    c54 = c50.clone()
    c55 = c50.clone()
    c56 = c50.clone()
    #Segunda fila
    c40 = c50.clone()
    c41 = c50.clone()
    c42 = c50.clone()
    c43 = c50.clone()
    c44 = c50.clone()
    c45 = c50.clone()
    c46 = c50.clone()
    #Tercera fila
    c30 = c50.clone()
    c31 = c50.clone()
    c32 = c50.clone()
    c33 = c50.clone()
    c34 = c50.clone()
    c35 = c50.clone()
    c36 = c50.clone()
    #Cuarta fila
    c20 = c50.clone()
    c21 = c50.clone()
    c22 = c50.clone()
    c23 = c50.clone()
    c24 = c50.clone()
    c25 = c50.clone()
    c26 = c50.clone()
    #Quinta fila
    c10 = c50.clone()
    c11 = c50.clone()
    c12 = c50.clone()
    c13 = c50.clone()
    c14 = c50.clone()
    c15 = c50.clone()
    c16 = c50.clone()
    #Sexta fila
    c00 = c50.clone()
    c01 = c50.clone()
    c02 = c50.clone()
    c03 = c50.clone()
    c04 = c50.clone()
    c05 = c50.clone()
    c06 = c50.clone()

    #fila 1
    fila1 = [c50,c51,c52,c53,c54,c55,c56]
    for j in fila1:
        j.move(mx,0)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 2
    fila2 = [c40,c41,c42,c43,c44,c45,c46]
    for j in fila2:
        j.move(mx,8)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 3
    fila3 = [c30,c31,c32,c33,c34,c35,c36]
    for j in fila3:
        j.move(mx,16)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 4
    fila4 = [c20,c21,c22,c23,c24,c25,c26]
    for j in fila4:
        j.move(mx,24)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    my = 10.33
    # Fila 5
    fila5 = [c10,c11,c12,c13,c14,c15,c16]
    for j in fila5:
        j.move(mx,32)
        j.setFill(color_rgb(239,231,218))
        j.setOutline(color_rgb(239,231,218))
        j.draw(win)
        mx = mx + 10.2
    mx = 10.2
    #fila 6
    fila6 = [c00,c01,c02,c03,c04,c05,c06]
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

    
    # Funcion que ejecuta el juego
    connect4(win, fila1, fila2, fila3, fila4, fila5,fila6,errorTxt)
    
    win.getMouse()
    win.close()

    

# ----------------------------------------------Juego no grafico----------------------------------------------

# ----------------------------------------------Se añade la pieza al board----------------------------------------------
def movimiento(board, jugada, turno, filas, i, win,fila1, fila2, fila3, fila4, fila5,fila6):
    board[filas-i][jugada-1] = turno
    print("\n",filas-i, " ", jugada-1)
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()
    if turno == 1:
        teamcolor = color_rgb(150,2,0) #Color rojo (Jugador1)
    else:
        teamcolor = color_rgb(245,203,92) #Color amarrillo (Jugador2)

    
    for u in range(7):
        if filas-i == 5 and jugada-1 == u:   #Fila 1
            fila1[u].setFill(teamcolor) 
            fila1[u].setOutline(teamcolor)
            
    for u in range(7):
        if filas-i == 4 and jugada-1 == u:   #Fila 2
            fila2[u].setFill(teamcolor) 
            fila2[u].setOutline(teamcolor)
            
    for u in range(7):
        if filas-i == 3 and jugada-1 == u:   #Fila 3
            fila3[u].setFill(teamcolor) 
            fila3[u].setOutline(teamcolor)

    for u in range(7):
        if filas-i == 2 and jugada-1 == u:   #Fila 4
            fila4[u].setFill(teamcolor) 
            fila4[u].setOutline(teamcolor)

    for u in range(7):
        if filas-i == 1 and jugada-1 == u:   #Fila 5
            fila5[u].setFill(teamcolor) 
            fila5[u].setOutline(teamcolor)

    for u in range(7):
        if filas-i == 0 and jugada-1 == u:   #Fila 6
            fila6[u].setFill(teamcolor) 
            fila6[u].setOutline(teamcolor)
    

# ----------------------------------------------Se reciben los input de los jugadores y se valida que el mismo entre un numero entero----------------------------------------------
def validacion_entradas(jugada, jugador, win,errorTxt):
    while True:
        try:
            while True:
                textturno = Text(Point(49,65), jugador + ' entre el numero de la columna que desea ubicar su ficha')
                textturno.draw(win)
                jugada = int(win.getKey())
                while jugada < 1 or jugada > 7:
                    errorTxt.setText('El valor entrado no es valido. Vuelva a intentarlo.')
                    jugada = int(win.getKey())
                    errorTxt.setText('')
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
def proximo_espacio_disponible(board, jugada, turno, filas,errorTxt):
    i = 1
    while True:

        while board[filas-i][jugada-1] != 0:
            i = i + 1
            if i > 6:
                errorTxt.setText('Esta columna ya esta llena. Intente en otra.')
                i = 8
                if turno == 1:
                    turno = 2
                else:
                    turno = 1
                break
        return i
        
# Se indentifica de quien es el turno y llama la funcion que permite la entrada de la columna que el jugador desea seleccionar         
def entradas(turno, jugada, win,errorTxt):
    jugada = 0
    if turno == 2:
        jugador = "Jugador #1"
        turno = 1 
    else:
        jugador = "Jugador #2"
        turno = 2

    jugada = validacion_entradas(jugada, jugador, win,errorTxt)
    # if jugada < 1 or jugada > 7:
    #     errorTxt.setText('El valor entrado no es valido. Vuelva a intentarlo.')
    #     while jugada < 1 or jugada > 7:
    #         jugada = validacion_entradas(jugada, jugador,win,errorTxt)
    return jugada, turno

def columnaLlena():
    pass

# Funcion que verifica si en alguna parte de la matriz hay un ganador
def verificar_ganador(board, jugada, turno):
    #Verificar verticalmente
    try:
        for i in range(6):
            for j in range(7):
                if board[i][j] == turno and board[i+1][j] == turno and board[i+2][j] == turno and board[i+3][j] == turno:
                    return 4
    except IndexError:
        print('No se encontro un ganador verticalmente')

    #Verificar horizontalmente
    try:
        for i in range(6):
            for j in range(7):
                if board[i][j] == turno and board[i][j+1] == turno and board[i][j+2] == turno and board[i][j+3] == turno:
                    return 4
    except IndexError:
        print('No se encontro un ganador horizontalmente')

    #Verificar diagonal hacia atras
    try:
        for i in range(6):
            for j in range(7):
                if board[i][j] == turno and board[i+1][j+1] == turno and board[i+2][j+2] == turno and board[i+3][j+3] == turno:
                    return 4
    except IndexError:
        print('No se encontro un ganador de forma diagonal hacia atras')
    
    #Verificar diagonal hacia atras
    try:
        for i in range(6):
            for j in range(7):
                if board[i][j] == turno and board[i-1][j+1] == turno and board[i-2][j+2] == turno and board[i-3][j+3] == turno:
                    return 4
    except IndexError:
        print('No se encontro un ganador de forma diagonal hacia atras')

    # Si no hay ganador retorna falso
    return False

# Funcion que genera una pantalla grafica una vez halla un ganador
def pantalla_ganadora (win, turno):
    # Se selecciona el nombre del ganador
    if turno == 1:
        ganador = 'Jugador #1'
    else:
        ganador = 'Jugador #2'

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

# Funcion que ejecuta el juego de Connect 4
def connect4(win,fila1, fila2, fila3, fila4, fila5,fila6,errorTxt):
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
        # Se recibe y se valida el dato entrado por el jugador
        jugada, turno = entradas(turno, jugada, win,errorTxt)
        # Se identifica en que fila de la columna que eligio el jugador esta disponible
        i = proximo_espacio_disponible(board,jugada,turno, filas,errorTxt)

        while i == 8:
            if turno == 1:
                turno = 2
            else:
                turno = 1
            jugada, turno = entradas(turno, jugada, win,errorTxt)
            i = proximo_espacio_disponible(board,jugada,turno, filas,errorTxt)
        
        # Se registra el movimiento en la matriz y en la pantalla grafica
        movimiento(board,jugada,turno, filas, i, win,fila1, fila2, fila3, fila4, fila5,fila6)
        # Se verifica si hay un ganador
        finJuego = verificar_ganador(board, jugada, turno)

    #Llamado a la funcion que crea una pantalla anunciando al ganador    
    pantalla_ganadora(win, turno)
main()


            
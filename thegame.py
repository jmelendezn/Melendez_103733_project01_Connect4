from graphics import *
class Connect4:
    def __init__ (self,win,fila1, fila2, fila3, fila4, fila5,fila6,errorTxt):
        self.win = win
        self.fila1 = fila1
        self.fila2 = fila2
        self.fila3 = fila3
        self.fila4 = fila4
        self.fila5 = fila5
        self.fila6 = fila6
        self.errorTxt = errorTxt
        self.columnas = 7
        self.filas = 6
        self.finJuego = 0
        self.turno = 2
        self.jugada = 0
        self.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.i = 0
    def the_game(self):
        
        for row in self.board:
            for elem in row:
                print(elem, end=' ')
            print()

        #Entrada de turnos
        while self.finJuego != 4:
            # Se recibe y se valida el dato entrado por el jugador
            self.jugada, self.turno = self.entradas()
            # Se identifica en que fila de la columna que eligio el jugador esta disponible
            self.i = self.proximo_espacio_disponible()

            while self.i == 8:
                if self.turno == 1:
                    self.turno = 2
                else:
                    self.turno = 1
                self.jugada, self.turno = entradas(self.turno, self.jugada, self.win,self.errorTxt)
                self.i = proximo_espacio_disponible(self.board,self.jugada,self.turno, self.filas,self.errorTxt)
            
            # Se registra el movimiento en la matriz y en la pantalla grafica
            self.movimiento()
            # Se verifica si hay un ganador
            self.finJuego = self.verificar_ganador()

        #Llamado a la funcion que crea una pantalla anunciando al ganador    
        self.pantalla_ganadora()
    
    def entradas(self):
        self.jugada = 0
        if self.turno == 2:
            self.jugador = "Jugador #1"
            self.turno = 1 
        else:
            self.jugador = "Jugador #2"
            self.turno = 2

        self.jugada = self.validacion_entradas()
    
        return self.jugada, self.turno

    # Se reciben los input de los jugadores y se valida que el mismo entre un numero entero
    def validacion_entradas(self):
        while True:
            try:
                while True:
                    textturno = Text(Point(49,65), self.jugador + ' entre el numero de la columna que desea ubicar su ficha')
                    textturno.draw(self.win)
                    self.jugada = int(self.win.getKey())
                    while self.jugada < 1 or self.jugada > 7:
                        self.errorTxt.setText('El valor entrado no es valido. Vuelva a intentarlo.')
                        self.jugada = int(self.win.getKey())
                        self.errorTxt.setText('')
                    textturno.setText(' ')
                    self.errorTxt.setText(' ')
                    return  self.jugada
            except ValueError:
                self.errorTxt.setText('El valor entrado no es valido. Vuelva a intentarlo.')
                textturno.setText(' ')
                continue
            else:
                return  self.jugada
            break
    
    def proximo_espacio_disponible(self):
        i = 1
        while True:

            while self.board[self.filas-i][self.jugada-1] != 0:
                i = i + 1
                if i > 6:
                    self.errorTxt.setText('Esta columna ya esta llena. Intente en otra.')
                    i = 8
                    if self.turno == 1:
                        self.turno = 2
                    else:
                        self.turno = 1
                    break
            return i

    def movimiento(self):
        self.board[self.filas-self.i][self.jugada-1] = self.turno
        print("\n",self.filas-self.i, " ", self.jugada-1)
        for row in self.board:
            for elem in row:
                print(elem, end=' ')
            print()
        if self.turno == 1:
            teamcolor = color_rgb(150,2,0) #Color rojo (Jugador1)
        else:
            teamcolor = color_rgb(245,203,92) #Color amarrillo (Jugador2)

        
        for u in range(7):
            if self.filas-self.i == 5 and self.jugada-1 == u:   #Fila 1
                self.fila1[u].setFill(teamcolor) 
                self.fila1[u].setOutline(teamcolor)
                
        for u in range(7):
            if self.filas-self.i == 4 and self.jugada-1 == u:   #Fila 2
                self.fila2[u].setFill(teamcolor) 
                self.fila2[u].setOutline(teamcolor)
                
        for u in range(7):
            if self.filas-self.i == 3 and self.jugada-1 == u:   #Fila 3
                self.fila3[u].setFill(teamcolor) 
                self.fila3[u].setOutline(teamcolor)

        for u in range(7):
            if self.filas-self.i == 2 and self.jugada-1 == u:   #Fila 4
                self.fila4[u].setFill(teamcolor) 
                self.fila4[u].setOutline(teamcolor)

        for u in range(7):
            if self.filas-self.i == 1 and self.jugada-1 == u:   #Fila 5
                self.fila5[u].setFill(teamcolor) 
                self.fila5[u].setOutline(teamcolor)

        for u in range(7):
            if self.filas-self.i == 0 and self.jugada-1 == u:   #Fila 6
                self.fila6[u].setFill(teamcolor) 
                self.fila6[u].setOutline(teamcolor)

    # Funcion que verifica si en alguna parte de la matriz hay un ganador
    def verificar_ganador(self):
        #Verificar verticalmente
        try:
            for i in range(6):
                for j in range(7):
                    if self.board[i][j] == self.turno and self.board[i+1][j] == self.turno and self.board[i+2][j] == self.turno and self.board[i+3][j] == self.turno:
                        return 4
        except IndexError:
            print('No se encontro un ganador verticalmente')

        #Verificar horizontalmente
        try:
            for i in range(6):
                for j in range(7):
                    if self.board[i][j] == self.turno and self.board[i][j+1] == self.turno and self.board[i][j+2] == self.turno and self.board[i][j+3] == self.turno:
                        return 4
        except IndexError:
            print('No se encontro un ganador horizontalmente')

        #Verificar diagonal hacia atras
        try:
            for i in range(6):
                for j in range(7):
                    if self.board[i][j] == self.turno and self.board[i+1][j+1] == self.turno and self.board[i+2][j+2] == self.turno and self.board[i+3][j+3] == self.turno:
                        return 4
        except IndexError:
            print('No se encontro un ganador de forma diagonal hacia atras')
        
        #Verificar diagonal hacia atras
        try:
            for i in range(6):
                for j in range(7):
                    if self.board[i][j] == self.turno and self.board[i-1][j+1] == self.turno and self.board[i-2][j+2] == self.turno and self.board[i-3][j+3] == self.turno:
                        return 4
        except IndexError:
            print('No se encontro un ganador de forma diagonal hacia atras')

        # Si no hay ganador retorna falso
        return False

    # Funcion que genera una pantalla grafica una vez halla un ganador
    def pantalla_ganadora (self):
        # Se selecciona el nombre del ganador
        if self.turno == 1:
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
            i.draw(self.win)
# ----------------------------------------------Pantalla grafica----------------------------------------------
def main():
    #Se crea la pantalla grafica
    win = GraphWin('Game', 800,900)
    win.setCoords(0,0,100,100)

    # Se llama la funcion que dibuja el juego
    fila1, fila2, fila3, fila4, fila5,fila6,errorTxt = dibujar_juego(win)
    
    # Funcion que ejecuta el juego
    game = Connect4(win, fila1, fila2, fila3, fila4, fila5,fila6,errorTxt)
    game.the_game()
    
# def __init__ (self,win,fila1, fila2, fila3, fila4, fila5,fila6,errorTxt):

    win.getMouse()
    win.close()

    
# ----------------------------------------------Se añade la pieza al board----------------------------------------------
def dibujar_juego(win):
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

    return fila1, fila2, fila3, fila4, fila5,fila6,errorTxt



main()

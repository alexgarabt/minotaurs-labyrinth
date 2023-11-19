from src.labyrinth.Partida import Partida
from src.twodimension.Point import Point

FILE_NAME = 'entrada.txt'

def readFile():
    stringFile = []
    with open(FILE_NAME,'r') as file:
         for line in file:
            line = line.strip('\n')
            stringFile.append(line)
    return stringFile

def crearListaPartida(arrayPartidas):
    aux = arrayPartidas[0].split(' ')
    aux = [int(i) for i in aux]
    longPartida = aux[0]+aux[1]
    partidaArray = []
    resto = []
    for i in range(len(arrayPartidas)):
        if(i != 0):
            if(i <= longPartida+1):
                partidaArray.append(arrayPartidas[i])
            else:
                resto.append(arrayPartidas[i])
    return partidaArray,resto
        
def convertirPuntos(laberinto):
    listaPuntos = []
    for i in range(len(laberinto)):
        if(i != len(laberinto)-1):
            aux = i.split(' ')
            aux = [float(i) for i in aux]
            listaPuntos.append(Point(aux[0],aux[1]))
        else:
            aux = i.split(' ')
            aux = [float(i) for i in aux]
            posicionActual = Point(aux[0], aux[1])   
    return listaPuntos, posicionActual    
    
def partidas(array):
    
    laberinto = crearListaPartida(array)[0]
    resto = crearListaPartida(array)[1]
    
    print("esta en una partida")
    laberinto = convertirPuntos(laberinto)
    juego = Partida(laberinto[0],laberinto[1])
    #resolver partida
    
    if(resto[0] == '-1 -1'):
        print("Fin de juego")
        return None
    else:
        return resto
    
def main():
    
    arrayPartidas = readFile()
    resto = partidas(arrayPartidas) 
    while(resto != None):
        resto = partidas(resto)
        

    

if __name__ == "__main__":
    main()

#Ejemplo, distancia entre dos puntos

class Coordenada:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self, otra_coord):
        dif_x = (self.x - otra_coord.x)**2
        dif_y = (self.y - otra_coord.y)**2
        return (dif_x + dif_y)**0.5


if __name__ == '__main__':
    coord1 = Coordenada(3,36)
    coord2 = Coordenada(12,95)

    #Imprimiendo distancia
    print(coord1.distancia(coord2))
    print(coord2.distancia(coord1))       

    #Verificando si el primer parametro es una instancia del segundo.
    print(isinstance(coord1, Coordenada))
    print(isinstance(4,Coordenada))

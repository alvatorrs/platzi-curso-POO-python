#Ejemplo herencia

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


'''
La forma en la que extendemos o heredamos el 
comportamiento de la subclase es introduciendo
como parametro a la superclase. 
'''
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())
    print('')
    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())


#Ejemplo polimorfismo

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} esta caminando...')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    #Aplicando polimorfismo
    def avanza(self):
        print(f'{self.nombre} esta baikiando...')


def main():
    persona = Persona('Alvaro')
    persona.avanza()

    ciclista = Ciclista('Onodera')
    ciclista.avanza()

if __name__ == '__main__':
    main()


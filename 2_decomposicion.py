#Ejemplo de cómo decomponer

class Automovil:

    def __ini__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'En reposo'
        self._motor = Motor(cilindros = 4) 

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyectar_gasolina(10)
        else:
            self._motor.inyectar_gasolina(3) 

        self._estado = 'en movimiento'


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def inyectar_gasolina(self, cantidad):
        pass

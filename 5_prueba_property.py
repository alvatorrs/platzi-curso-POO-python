class Prueba:
    def __init__(self, nombre):
        self._saludo = 'Hola'
        self.__despedida = 'Adios'
        self.nombre = nombre
        
    def _bienvenida(self):
        print(f'\nHola {self.nombre} bienvenido')
        print('Saludo:',self._saludo)
        print('Despedida',self.__despedida)

    #getter
    def get_despedida(self):
        print('Getter')
        return self.__despedida

    #setter
    def set_despedida(self,valor):
        print('Setter')
        self.__despedida = valor

    despedida = property(get_despedida, set_despedida)


#Creamos un objeto
sujeto = Prueba('Miguelon')
#Se puede acceder
print(sujeto._saludo)

try:
    print(sujeto.__despedida)
except: 
    print('No se puede acceder a despedida\n')


#Indicamos la despedida
print(sujeto.despedida)
sujeto.despedida = 'Bye bye'

sujeto._bienvenida()

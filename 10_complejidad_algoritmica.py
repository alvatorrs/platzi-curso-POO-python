#Cronometrar

from time import time
import sys

#primera implementación
def factorial_iterativo(n):
    respuesta = 1
    if n == 0:
        return respuesta
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


#segunda implementción
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)


if __name__ == '__main__':
    n = 1000

    print('Límite re recursión:',sys.getrecursionlimit())
    sys.setrecursionlimit(1100)
    print('Nuevo límite:',sys.getrecursionlimit())

    comienzo = time()
    factorial_iterativo(n)
    final = time()
    print(f'Para el factorial iterativo tomo: {final - comienzo}')

    comienzo = time()
    factorial_recursivo(n)
    final = time()
    print(f'Para el factorial recursivo tomo: {final - comienzo}')

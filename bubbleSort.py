# 1) Comenzar a hacer comparaciones de elementos adyacentes
# 2) Repetir haste tener una pasada completa sin ningun swap
from random import randint
# import csv


def bubbleSort(lista):
    n = len(lista)

    for i in range(n):
        cambios = False
        print(lista) #print statement
        for j in range(n -1 -i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                cambios = True
        if  not cambios:
            break
    return lista


if __name__ == '__main__':
    size = int(input('Seleccione un número de elementos: '))
    lista = [randint(0,100) for _ in range(size)]
    print(lista,'<-- Desordenada')
    resultado = bubbleSort(lista)
    print(resultado,'<-- Ordenada')

#     with open('numeros.csv','r') as f:
        # tabla = []
        # for renglon in csv.reader(f):
            # tabla.append(renglon)



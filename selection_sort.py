# 1) Buscar el número menor en mi array
# 2) Crear dos subarryas para llevar el contador de mi algoritmo
# 3) Imprimir el resultado del ordenamiento

from random import randint

def selectionSort(lista):
    #recorrer toda la lista
    for i in range(len(lista)):
        print(lista) #print statement
        #Encontrar el valor mínimo de la lista desordenada
        indice = i
        for j in range(i+1, len(lista)):
            if lista[indice] > lista[j]:
                indice = j
        #Cambiando el mínimo elemento por el primer valor de la lista desordenada
        lista[i], lista[indice] = lista[indice], lista[i]
    return lista


if __name__ == '__main__':
    size = int(input('Introduzca una cantidad: '))
    lista = [randint(0,100) for _ in range(size)]
    print(lista, '<-- desordenada')
    resultado = selectionSort(lista)
    print(resultado, '<-- ordenada')

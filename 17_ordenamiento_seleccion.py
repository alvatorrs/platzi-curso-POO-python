#Ordenamiento de seleccion

from random import randint

def selection_sort(lista):
    #recorrer toda la lista
    for i in range(len(lista)):
        #Encontrar el valor mínimo de la lista desordenada
        indice = i
        for j in range(i+1, len(lista)):
            if lista[indice] > lista[j]:
                indice = j
        #Cambiando el mínimo elemento por el primer valor de la lista desordenada
        lista[i], lista[indice] = lista[indice], lista[i]
    return lista



if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista: '))

    lista = [randint(0,100) for _ in range(tamano_lista)]
    print(lista)

    lista_ordenada = selection_sort(lista)
    print(lista_ordenada)

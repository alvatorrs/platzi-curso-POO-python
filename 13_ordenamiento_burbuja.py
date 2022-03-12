#Ordenamiento de burbuja

from random import randint

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n - i - 1): 
#n-i representa n menos lo que ya recorrimos (el extremo derecho de la lista ya ordenado)
            if lista[j] > lista[j+1]: #comparamos indices adyacentes
                lista[j], lista[j+1] = lista[j+1], lista[j]
                #print(lista)
#Este detalle es para ver todo el recorrido de la lista ordenando los números 
    return lista


if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista: '))

    lista = [randint(0,100) for _ in range(tamano_lista)]
    print(lista)

    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada)

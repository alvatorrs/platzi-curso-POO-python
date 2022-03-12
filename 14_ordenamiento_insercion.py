#Ordenamiento por inserción

from random import randint

def insertion_sort(lista):
    
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        indice_actual = indice
#Si el elemento con un indice menos es mayor que el actual, entraremos a while
        while indice_actual > 0 and lista[indice_actual -1] > valor_actual:
            lista[indice_actual] = lista[indice_actual - 1] 
            indice_actual -= 1
        #Colocamos el elemento actual en su lugar
        lista[indice_actual] = valor_actual
    return lista



if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista: '))

    lista = [randint(0,100) for _ in range(tamano_lista)]
    print(lista)

    lista_ordenada = insertion_sort(lista)
    print(lista_ordenada)

#Ordenamiento por mezcla

from random import randint

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2 #mitad lista
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda,'<->', derecha) ##
        
        #llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)
        #Iteradores para recorres sublistas
        i = 0
        j = 0
        #Iterador lista principal
        k = 0
        #Primeras comparaciones entre las dos listas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}') #
        print(lista) ##
        print('👾'*10) ##

    return lista

#los que tienen solo ## son print statement

if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista: '))

    lista = [randint(0,100) for _ in range(tamano_lista)]
    print(lista)
    print('-' * (4*tamano_lista))

    lista_ordenada = merge_sort(lista)
    print('-' * (4*tamano_lista)) ##
    print(lista_ordenada)

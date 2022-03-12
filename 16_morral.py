#El problema del morral
#Versión 0 - 1 knapsack (podemos tomar una cosa o no)

def morral(peso_morral, pesos, valores, n):
   #No hay artículos o se lleno el morral
    if n== 0 or peso_morral == 0: #caso base
        return 0
    #Un artículo ya no cabe en el morral
    if pesos[n-1] > peso_morral: #otro caso base
        return morral(peso_morral, pesos, valores, n-1)

    #Elección del artículo que nos de el mayor valor
    #max(tomar valor, no tomar valor)
    return max(valores[n-1] + morral(peso_morral - pesos[n-1], pesos, valores, n-1),
            morral(peso_morral, pesos, valores, n-1))


if __name__ == '__main__':
    valores = [60, 100, 120] #valores artículos
    pesos = [10, 20, 30] #tamaño artículos
    peso_morral = 30 #cupo del morral
    n = len(valores) #número de elementos (índice)

    resultado = morral(peso_morral, pesos, valores, n)         #valor máximos que podemos obtener
    print(resultado)

#Graficado simple

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html') #Generamos el outpt file
    fig = figure() #Generamos la primera figura que es donde se generan los graficos

    total_vals = int(input('Cuántos valores quieres gráficar? '))
    x_vals = list(range(total_vals))
    y_vals = []

    #Pedimos el valor de y por cada x generado anteriormente
    for x in x_vals:
        y = int(input(f'Valor de y para {x}: '))
        y_vals.append(y)

    fig.line(x_vals, y_vals, line_width=2) #Le decimos a la figura que genere una línea
    show(fig) #Le decimos que nos muestre la gráfica

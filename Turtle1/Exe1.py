# programa em python para demosntrar a serie de fibonacci
# espiral fractal usando a biblioteca Turtle
import turtle
import math


def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    x.pencolor("blue")

    # Desenhando o primeiro quadrado
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Continuando com a série
    temp = square_b
    square_b += square_a
    square_a = temp

    # Desenhando os outros quadrados
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        temp = square_b
        square_b += square_a
        square_a = temp

    # A caneta no ponto inicial da plotagem
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Definindo a cor da caneta para laranja
    x.pencolor("orange")

    # Espiral de Fibonacci
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


# 'factor' significa o multiplicativo
# fator que expande ou diminui a escala
# do gráfico por um determinado fator.
factor = 1

# Entrada para o número de
# Iterações que nosso algoritmo executará
n = int(input('Digite o número de iterações (deve ser > 1): '))

# Plotando a espiral
# e imprimindo o número de Fibonacci correspondente
if n > 0:
    print("Série de Fibonacci para", n, "elementos: ")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("O número de iterações deve ser > 0")

import turtle

# Método Screen() para obter a tela
wn = turtle.Screen()

# criando o objeto tess
tess = turtle.Turtle()


def triangle(x, y):
    # desenhar a caneta
    tess.penup()

    # é usado para mover o cursor em x
    # e na posição y
    tess.goto(x, y)

    # usado para desenhar a caneta
    tess.pendown()
    for i in range(3):
        # mover o cursor em 100 unidades
        # dígito para frente
        tess.forward(100)

        # girar o cursor 120 graus para a esquerda
        tess.left(120)

        # Mover o cursor em 100 unidades
        tess.forward(100)


# função especial integrada para enviar corrente
# posição do cursor para o triângulo
turtle.onscreenclick(triangle, 1)

turtle.listen()

# segure a tela
turtle.done()

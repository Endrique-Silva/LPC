from turtle import *

tam = int(input("Informe o tamanho da árvore e em seguida o nível: "))
niv = int(input())
speed('fastest')

# virando a tartaruga para cima
rt(-90)

# o ângulo agudo entre
# a base e o ramo do Y
angle = 30


# função para traçar um Y
def y(sz, level):
    if level > 0:
        colormode(255)

        # dividindo a faixa rgb para verde
        # em intervalos iguais para cada nível
        # definindo a cor de acordo
        # para o nível atual
        pencolor(0, 255 // level, 0)

        # desenhando a base
        fd(sz)

        rt(angle)

        # chamada recursiva para
        # a subárvore direita
        y(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        lt(2 * angle)

        # chamada recursiva para
        # a subárvore esquerda
        y(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)


# tree of size 80 and level 7
y(tam, niv)

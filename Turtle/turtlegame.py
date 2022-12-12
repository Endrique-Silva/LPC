import turtle
import random

turtle_one = turtle.Turtle()
turtle_one.color("green")
turtle_one.shape("turtle")
turtle_one.penup()
turtle_one.goto(-200,100)
turtle_two = turtle_one.clone()
turtle_two.color("blue")
turtle_two.penup()
turtle_two.goto(-200,-100)

turtle_one.goto(300,60)
turtle_one.pendown()
turtle_one.circle(40)
turtle_one.penup()
turtle_one.goto(-200,100)
turtle_two.goto(300,-140)
turtle_two.pendown()
turtle_two.circle(40)
turtle_two.penup()
turtle_two.goto(-200,-100)

die = [1,2,3,4,5,6]

for i in range(20):
    if turtle_one.pos() >= (300,100):
        print("O jogador Um é o vencedor!")
        break
    elif turtle_two.pos() >= (300,100):
        print("Jogador Dois é o vencedor!")
        break
    else:
        turtle_one_turn = input("Pressione 'Enter' para jogar o dado")
        die_outcome = random.choice(die)
        print("O resultado do dado é: ")
        print(die_outcome)
        print("O número de passos será de: ")
        print(20*die_outcome)
        turtle_one.fd(20*die_outcome)
        turtle_two_turn = input("Pressione 'Enter' para jogar o dado")
        die_outcome = random.choice(die)
        print("O resultado do dado é: ")
        print(die_outcome)
        print("O número de passos será de: ")
        print(20*die_outcome)
        turtle_two.fd(20*die_outcome)

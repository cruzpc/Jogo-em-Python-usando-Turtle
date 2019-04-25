'''
Jogo em Python utilizando o módulo turtle
Ainda falta adicionar:
 - Um inimigo, uma idéia é colocar um inimigo que cria barreiras que ao colidir o jogador perde vida
 - Um menu e mostrador de tempo e pontos, assim como recorde
'''

import turtle
import math
import random
tela = turtle.Screen() # cria a tela

velocidade = 3

tela.bgcolor("green")

# Desenha tela

desenhador = turtle.Turtle()
desenhador.penup()
desenhador.setposition(-300, -300)
desenhador.pendown()
desenhador.pensize(3)
for side in range(4):
    desenhador.forward(600)
    desenhador.left(90)
desenhador.hideturtle()

player = turtle.Turtle()
player.color("black")
player.shape("triangle")
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
player.penup() # não desenha nada, levantou a caneta por assim dizer

comida = turtle.Turtle()
comida.color("red")
comida.shape("circle")
comida.penup()
comida.setposition(-200, 100)



turtle.listen() # olhar as teclas por assim dizer
turtle.onkey(turnleft, "Left") # vira
turtle.onkey(turnright, "Right")

while True:
    player.forward(velocidade)
    # checar fronteiras
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
    # checar colisao com a comida
    d = math.sqrt(math.pow(player.xcor()-comida.xcor(), 2) + math.pow(player.ycor()-comida.ycor(), 2))
    if d < 20:
        comida.hideturtle()
        comida.setposition(random.randint(-300, 300), random.randint(-300, 300))
        comida.showturtle()

# for i in range(0, 100, 5):
#     pen.circle(i)

tela.exitonclick() # para parar a execução do programa no fim

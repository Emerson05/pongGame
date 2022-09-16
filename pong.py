import turtle
import os

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

pontuacao_a = 0
pontuacao_b = 0

objeto_a = turtle.Turtle()
objeto_a.speed(0)
objeto_a.shape("square")
objeto_a.color("#0AFA40")
objeto_a.shapesize(stretch_wid=5,stretch_len=1)
objeto_a.penup()
objeto_a.goto(-350,0)



objeto_b = turtle.Turtle()
objeto_b.speed(0)
objeto_b.shape("square")
objeto_b.color("#0AFA40")
objeto_b.shapesize(stretch_wid=5,stretch_len=1)
objeto_b.penup()
objeto_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#0AFA40")
ball.penup()
ball.goto(0,0)
ball.dx = 0.06
ball.dy = 0.06

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jogador A : 0 Jogador B : 0 ", align= "center", font=("Courier", 24, "normal"))

def objeto_a_subir():
    y = objeto_a.ycor()
    y += 20
    objeto_a.sety(y)

def objeto_a_descer():
    y = objeto_a.ycor()
    y -= 20
    objeto_a.sety(y)    

def objeto_b_subir():
    y = objeto_b.ycor()
    y += 20
    objeto_b.sety(y)

def objeto_b_descer():
    y = objeto_b.ycor()
    y -= 20
    objeto_b.sety(y)       

win.listen()

win.onkeypress(objeto_a_subir, "w")  
win.onkeypress( objeto_a_descer , "s")
win.onkeypress(objeto_b_subir, "Up")  
win.onkeypress( objeto_b_descer , "Down")  



while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        

    if ball.xcor() > 390:
        ball.goto(0, 0)    
        ball.dx *= -1
        pontuacao_a += 1
        pen.clear()
        pen.write("Jogador A : {} Jogador B : {} " .format(pontuacao_a, pontuacao_b), align= "center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)    
        ball.dx *= -1 
        pontuacao_b += 1
        pen.clear()
        pen.write("Jogador A : {} Jogador B : {} " .format(pontuacao_a, pontuacao_b), align= "center", font=("Courier", 24, "normal"))   

    if (ball.xcor()> 340 and ball.xcor() < 350 )and (ball.ycor() < objeto_b.ycor() + 50 and ball.ycor() > objeto_b.ycor()-40) :
        ball.setx(340)
        ball.dx *= -1 
         

    if (ball.xcor() < -340 and ball.xcor() > -350 )and (ball.ycor() < objeto_a.ycor() + 50 and ball.ycor() > objeto_a.ycor()-40) :
        ball.setx(-340)
        ball.dx *= -1  
             
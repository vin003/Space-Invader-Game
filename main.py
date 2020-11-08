import turtle
import os 

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")

#Draw Border
b_pen = turtle.Turtle()
b_pen.color("white")
b_pen.speed(0)
b_pen.penup()
b_pen.setposition(-300,-300)
b_pen.pendown()
for size in range(4):
    b_pen.fd(600)
    b_pen.lt(90)
b_pen.hideturtle()

##Create player 
player = turtle.Turtle()
player.color("blue")
player.penup()
player.setheading(90)
player.shape("triangle")
player.speed(0)
player.setposition(0,-250)

playerspeed = 15  
## move the player Left and Right 
def mov_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280 :
        x = 280
    player.setx(x)


def mov_right():
    x =player.xcor()
    x +=playerspeed
    if x > 280 :
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as global  if it need changed 

    
#Keboard bindings 
turtle.listen()
turtle.onkey(mov_left,"Left")
turtle.onkey(mov_right,"Right")

##Create enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.speed(0)
enemy.penup()
enemy.setposition(-300,250)  ## 2nd quadrant 
enemyspeed = 2 


##create a bullet oobect
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.speed(0)
bullet.color("yellow")
bullet.penup()
bullet.shapesize(0.5,0.5)
bullet.setheading(90)   
bullet.hideturtle()

bulletspeed = 20 
bulletstate = "ready"





##main programm
while True:
    ##move enemy 
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    ##boundary
    if enemy.xcor() > 280:
        enemyspeed *= -1
        y = enemy.ycor()
        y -= 40 
        enemy.ycor(y)
    elif enemy.xcor() < -280 :
        enemyspeed *=  -1
        y =enemy.ycor()
        y -=40 
        enemy.sety(y)
















wn.delay(input("pres q  exit: "))
#Space Invaders - Part 9
#Image for Invader
#Image for Player
#Image for background
# Python 2.7 on Mac
import turtle
import os
import math
import random
import pygame
import re

pygame.init

# Set up the screen
wn = turtle.Screen()
turtle.screensize(300, 300)
wn.bgcolor("black")
wn.title("REGEX INVADERS")
wn.bgpic("space.png")

# Register the shapes
turtle.register_shape("a.gif")
turtle.register_shape("b.gif")
turtle.register_shape("player.gif")

# Draw border
#border_pen = turtle.Turtle()
#border_pen.speed(0)
#border_pen.color("white")
#border_pen.penup()
#border_pen.setposition(-300,-300)
#border_pen.pendown()
#border_pen.pensize(3)
#for side in range(4):
#	border_pen.fd(600)
#	border_pen.lt(90)
#border_pen.hideturtle()	

# Set the score to " "
score = ""

problems = ["{w | the string contains 3 a's}","{w | the string starts with a and ends with b}","{w | the string has no a's}"]
regex = ["(a{3})*", "^a+b+$", "b*"]

rand_prob = problems[random.randrange(len(problems))]
# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-350, 290)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

problem_pen = turtle.Turtle()
problem_pen.speed(0)
problem_pen.color("white")
problem_pen.penup()
problem_pen.setposition(-290, -350)
probstring = "Problem: %s" %rand_prob
problem_pen.write(rand_prob, False, align="left", font=("Arial", 14, "normal"))
problem_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -300)
player.setheading(90)

playerspeed = 15

# Choose a number of enemies
number_of_enemies = 6
#Create an empty list of enemies
enemies = []



names = ['a.gif', 'b.gif']


# Add enemies to the list
for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	rand_item = names[random.randrange(len(names))]
	enemy.color("red")
	enemy.shape(rand_item)
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)
	

enemyspeed = 2


# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(1.5, 1.5)
bullet.hideturtle()

bulletspeed = 30

# Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


# Move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
	
def fire_bullet():
	#Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		#Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 20:
		return True
	else:
		return False
# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
	
	for enemy in enemies:
		#Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
			
		#Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			#Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#Update the score
			if enemy.shape() == 'a.gif':
				score = score + "a"
				print(score)
			elif enemy.shape() == 'b.gif':
				score = score + "b"
				print(score)
			scorestring = "Score: " + score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break

		
	#Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"


raw_input("Press enter to finsh.")

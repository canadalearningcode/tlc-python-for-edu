import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

t = turtle.Turtle()
t.shape('turtle')
t.speed(10)


screen = turtle.Screen()
screen.bgcolor('black')


for x in range(50):
  color = random.choice(colors)
  t.color(color)

  t.forward(120 + x)
  t.right(141)
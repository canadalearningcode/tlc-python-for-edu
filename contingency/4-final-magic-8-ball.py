from processing import *
import random

def setup():
  size(300,300) # Size of our sketch
  strokeWeight(3)


def draw():
    background(100, 100, 100)

    fill(000,000,000)
    ellipse(150, 150, 200, 200)

    fill(255,255,255)
    ellipse(150, 150, 100, 100)

    ellipse(150, 135, 30, 30)
    ellipse(150, 165, 30, 30)

    text("Welcome to Magic 8 Ball Simulator", 60, 30)
    text("Ask me a question, then click me for the answer!", 25, 275)

def mouseClicked():
    answers = [
    'Yes, definitely', 
    'Ask again', 
    'No, absolutely not', 
    'Maybe', 
    "Yes", 
    'No', 
    'Probably'
    ]

    print(random.choice(answers))


run()
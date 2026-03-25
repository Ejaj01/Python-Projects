import turtle
import time
import random

WIDTH, HEIGHT = 800, 600
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown"] 

def get_the_number_of_racers():
    racers = 0
    
    while True:
        racers = input("Enter The Number Of Racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not a valid number. Try again!")
            continue

        if 2 <= racers <= 10:
                return racers
        else:
            print("Please enter a number between 2 and 10!")
            continue

def race(colors):
     turtles = create_turtles(colors)

     while True:
            for racer in turtles:
                distance = random.randint(1, 20)
                racer.forward(distance)

                x, y = racer.position()
                if y >= HEIGHT // 2 - 10:
                     return colors[turtles.index(racer)]
    

def create_turtles(colors):
     turtles = []
     spacing = WIDTH // (len(colors) + 1)
     for i, color in enumerate(colors):
          racer = turtle.Turtle()
          racer.color(color)
          racer.shape("turtle")
          racer.left(90)
          racer.penup()
          racer.setpos(-WIDTH // 2 + (i + 1) * spacing, -HEIGHT // 2 + 20)
          racer.pendown()
          turtles.append(racer)
     return turtles





def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")

racers = get_the_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner is: {winner}!")
turtle.done()

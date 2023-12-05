from turtle import Turtle, Screen
import random
import time

import sys
sys.setrecursionlimit(10**9)

colors = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'brown', 'orange']
cars = []


class MyTurtleCharacter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.reset_position()

    def reset_position(self):
        self.goto(x=0, y=-370)

    def move_forward(self):
        print("moving forward")
        self.forward(10)

    def move_backwards(self):
        print("moving forward")
        self.backward(10)
    # def check_if_turtle_crossed_top(self):


class car(Turtle):
    def __init__(self, colors_list):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.goto(x=300, y=random.randint(-340, 340))
        self.shape('square')
        self.color(random.choice(colors_list))
        self.shapesize(stretch_len=2)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 0
        self.add_level()

    def collision(self, my_turtle, cars):
        for car in cars:
            distance = my_turtle.distance(car)
            if distance <= 25:
                print("Collision detected")
                return True

    # def game_over
    def add_level(self):
        self.level += 1
        self.clear()
        self.goto(x=-260, y=340)
        self.write(f"Level: {self.level}", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(x=-120, y=0)
        self.write("Game Over", font=("Arial", 35, "normal"))


def create_new_car_and_move_it(colors_list):
    global cars
    if random.randint(0, 6) == 1:
        new_car = car(colors_list=colors_list)
        cars.append(new_car)
    for carr in cars:
        carr.forward(10)
        if carr.pos()[0] < -300:
            print("car removed")
            carr.hideturtle()
            cars.remove(carr)


def game_loop(sleeptime):
    time.sleep(sleeptime)
    screen.onkey(my_turtle.move_forward, "Up")
    screen.onkey(my_turtle.move_backwards, "Down")
    create_new_car_and_move_it(colors)
    if my_turtle.pos()[1] >= 370:
        my_turtle.reset_position()
        scoreboard.add_level()
        sleeptime *= 0.75

    print(sleeptime)
    screen.update()
    if not scoreboard.collision(my_turtle, cars):
        game_loop(sleeptime)
    # Scoreboard.game_over()
    # if my_turtle.ycor()
    scoreboard.game_over()


def edit_screen(screenn):
    screenn.tracer(False)
    screenn.title("Turtle Crossing Game By Omar Sarsar")
    screenn.setup(width=600, height=800)
    screenn.bgcolor("black")


sleeptime = 0.15
# Screen Creation
screen = Screen()
edit_screen(screen)

scoreboard = Scoreboard()

my_turtle = MyTurtleCharacter()
screen.listen()

game_loop(sleeptime)

screen.exitonclick()

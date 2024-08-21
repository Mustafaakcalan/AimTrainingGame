import turtle
import random

screen = turtle.Screen()
screen.title("Aim Training")
game_over = False
score = 0
FONT = ('Arial', 30, 'normal')
screen.bgcolor("light blue")

turtle_list = []
score_turtle = turtle.Turtle()
count_down_turtle = turtle.Turtle()

def make_score_turtle():
    score_turtle.color("blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    score_turtle.setposition(0, y)
    score_turtle.write(arg='Score 0', move=False, align='center', font=FONT)

grid_size = 10

def make_target(x, y):
    target = turtle.Turtle()
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), move=False, align='center', font=FONT)
        print(x, y)
    target.onclick(handle_click)
    target.penup()
    target.shape("circle")
    target.shapesize(1.7, 1.7)
    target.color("red")
    target.goto(x * grid_size, y * grid_size)
    target.pendown()
    turtle_list.append(target)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, 10, 0, -10, 20]

def setup_target():
    for x in x_coordinates:
        for y in y_coordinates:
            make_target(x, y)

def hide_targets():
    for target in turtle_list:
        target.hideturtle()

def show_targets_randomly():
    if not game_over:
        hide_targets()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_targets_randomly, 600)

def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_targets()
        count_down_turtle.write("Game Over!", align='center', font=FONT)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    make_score_turtle()
    setup_target()
    hide_targets()
    show_targets_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()

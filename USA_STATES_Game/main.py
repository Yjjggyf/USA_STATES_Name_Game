from turtle import Turtle, Screen

import pandas

turtle = Turtle()
screen = Screen()
screen.title("Usa_States_Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
import pandas as pd

my_data = pd.read_csv("50_states.csv")
states = my_data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                   prompt="What's another state's name").title()
    print(user_answer)

    correct_answer_row = my_data[my_data.state == user_answer]
    if user_answer == "Exit":

        break

    if user_answer in states:
        tim = Turtle()
        guessed_states.append(user_answer)
        tim.hideturtle()
        tim.penup()
        tim.setposition(correct_answer_row.x.item(), correct_answer_row.y.item())
        tim.write(user_answer)
        tim.home()
new_list = []
for answer in guessed_states:
    for state in states:
        if state != answer:
            new_list.append(state)
new_data = pandas.DataFrame(new_list)
new_data.to_csv("State to learn.csv")


import turtle
import pandas
from print_name import PrintName


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_cour(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cour)

data = pandas.read_csv("./50_states.csv")
title = "Guess the State"
state_list = data.state.tolist()
guessed_count = 0
guessed_states = {
    "State": []
}

game_is_on = True

while game_is_on:
    if guessed_count != 0:
        title = f"{guessed_count}/50 States Correct"
    answer_state = (screen.textinput(title=title, prompt="What's the name of State?")).title()
    if answer_state in state_list:
        guessed_count += 1
        state = data[data.state == answer_state]
        x_cor = int(state.x)
        y_cor = int(state.y)
        new_state = PrintName((x_cor, y_cor), answer_state)
        new_state.show_name()
        guessed_states["State"].append(answer_state)
        states_data = pandas.DataFrame(guessed_states)
        states_data.to_csv("./guessed_states.csv")
    if guessed_count == 50:
        game_is_on = False


turtle.mainloop()

# screen.exitonclick()

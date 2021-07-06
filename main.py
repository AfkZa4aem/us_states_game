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
guessed_states = []

game_is_on = True

while len(guessed_states) < 50:
    if len(guessed_states) != 0:
        title = f"{len(guessed_states)}/50 States Correct"
    answer_state = (screen.textinput(title=title, prompt="What's the name of State?")).title()
    if answer_state in guessed_states:
        pass
    elif answer_state in state_list:
        state = data[data.state == answer_state]
        x_cor = int(state.x)
        y_cor = int(state.y)
        new_state = PrintName((x_cor, y_cor), answer_state)
        new_state.show_name()
        guessed_states.append(answer_state)
    if len(guessed_states) >= 50 or answer_state == "Exit":
        not_guessed_states = [item for item in state_list if item not in guessed_states]
        states_data = pandas.DataFrame(not_guessed_states)
        states_data.to_csv("./states_to_learn.csv")
        break


# turtle.mainloop()

# screen.exitonclick()

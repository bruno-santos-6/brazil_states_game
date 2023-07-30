import turtle
import pandas as pd
from unidecode import unidecode
import re

screen = turtle.Screen()
screen.title("Brazil's States Game")
image = "./conversion_png_gif/Brazil_Labelled_Map.gif"
screen.addshape(image)
turtle.shape(image)

# Code for detecting the x and y coordinates of each state in the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# Function to remove accents and replace special characters
def remove_accents_and_special_characters(text):
    # Remove accents using unidecode
    text_without_accents = unidecode(text)

    # Replace special characters with empty space
    pattern = r'[^A-Za-z0-9 ]'
    text_without_special_chars = re.sub(pattern, '', text_without_accents)

    return text_without_special_chars


def remove_accentuation(text):
    return unidecode(text)


data = pd.read_csv("27_states.csv")
data["state"] = data["state"].apply(remove_accentuation)
data["state"] = data.state.str.lower()

all_states = data.state.apply(remove_accents_and_special_characters).to_list()
all_states = [x.lower() for x in all_states]

guessed_states = []

while len(guessed_states) < 27:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27 States Correct",
                                    prompt="What's another state name?")
    answer_state_refined = remove_accents_and_special_characters(answer_state).lower()

    if answer_state_refined == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state_refined in all_states:
        guessed_states.append(answer_state_refined)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state_refined]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

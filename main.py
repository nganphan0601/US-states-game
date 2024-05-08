import turtle as t
import pandas as pd


screen = t.Screen()
screen.title("U.S. States Game")

# load the image to be the shape
img = "blank_states_img.gif"
screen.addshape(img)

# set the turtle object's shape to be the image
t.shape(img)

# read the csv
data = pd.read_csv('50_states.csv')
all_states = data["state"].to_list()    # Get a list of the states
# get the user's input for guessing
correct_states = 0
guessed_states = []

while correct_states < 51:
    answer_state = screen.textinput(title=f'{correct_states}/50 States correct', 
                                    prompt="What's another state's name of the US?").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            missing_states.append(state) if state not in guessed_states else None
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv('missing_states.csv')
        break
    
    if answer_state in all_states:
        state_data = data[data["state"] == answer_state]   
        x = state_data.x.to_list()[0]
        y = state_data.y.to_list()[0]
        location = t.Turtle()
        location.hideturtle()
        location.penup()
        location.goto(x, y)
        location.write(state_data.state.item())
        guessed_states.append(answer_state)
        correct_states += 1


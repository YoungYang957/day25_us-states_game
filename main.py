import turtle
import pandas
screen =turtle.Screen()
screen.title("U.S States Gmae")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answer_state = screen.textinput(title= "Guess the state", prompt="Whats another state name?").title()

guess_state = []

while len(guess_state) <50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 correct", prompt="Whats another state name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guess_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states to learn")
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)







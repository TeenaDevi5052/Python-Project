import turtle as t
import pandas
screen=t.Screen()
canvas=screen.getcanvas()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
t.shape("blank_states_img.gif")
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(f"{len(guessed_states)}/50 Guessed States","Mention State's Name:").title()
    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        print(missing_state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("Learn_from_Here.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t1=t.Turtle()
        t1.hideturtle()
        t1.penup()
        state_data=data[data.state==answer_state]
        t1.goto(state_data.x.item(),state_data.y.item())
        t1.write(answer_state)



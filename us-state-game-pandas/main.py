import turtle
import pandas
screen=turtle.Screen()
screen.title('Guess the States')
image='./blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_data=pandas.read_csv('./50_states.csv')
state_list=states_data['state'].to_list()
# def check_answer(answer_state):
state_score=0
while state_score<50:
    answer_state = screen.textinput(title='Enter state name', prompt='Whats other states names?')
    if answer_state in state_list:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_score+=1
        state_location=states_data[states_data.state==answer_state]
        t.goto(float(state_location.x),float(state_location.y))
        t.write(answer_state)
        print(state_location, state_score)
turtle.mainloop()
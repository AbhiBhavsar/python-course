from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pngImg=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=pngImg)
canvas.create_text(103,132,text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

#========= Title Label ======
main_title=canvas.create_text(row=0,column=2, text='Timer', fill=GREEN, font=(FONT_NAME, 45, 'bold'))
main_title.grid(row=0,col=2)
canvas.grid()
window.mainloop()
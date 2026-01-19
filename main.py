from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_txt, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break)
        timer.config(text="Break 😴", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break)
        timer.config(text="Break 🤩", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work 🤠", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += "✔"
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(107, 133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)

tick = Label(fg=GREEN, highlightthickness=0, bg=YELLOW)
tick.grid(column=1, row=3)

window.mainloop()

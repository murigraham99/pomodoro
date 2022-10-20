import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_for_reset = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_for_reset)
    timer_text.config(text="Timer")
    tick.config(text="")
    canvas.itemconfig(timer, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Short (5 min) break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Long (20 min) break", fg=RED)

    else:
        count_down(work_sec)
        timer_text.config(text="Focus Mode (25 min)", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer_for_reset
        timer_for_reset = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        symbol = ""
        for _ in range(math.floor(reps / 2)):  # no of work session
            symbol += "✓ "
        tick.config(text=symbol)


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Pomodoro technique")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(row=1, column=1)

timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))

timer_text = Label()
timer_text.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_text.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, bd=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, bd=0, command=reset_timer)
reset_button.grid(row=2, column=2)
tick = Label(text=" ", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
tick.grid(row=3, column=1)

window.mainloop()

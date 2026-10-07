import tkinter as tk
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#84c3e1"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
running = False
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer, running
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    running = False
    check_sign["text"] = ""
    start_button.config(state=tk.NORMAL)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global running
    if running:
        return
    running = True
    start_button.config(state=tk.DISABLED)
    next_session()

def next_session():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        label["text"] = "Rest"
        label["fg"] = RED
    elif reps % 2 == 0:
        count_down(short_break_secs)
        label["text"] = "Rest"
        label["fg"] = PINK
    else:
        count_down(work_secs)
        label["text"] = "Work"
        label["fg"] = BLUE
    completed = (reps // 2) % 4
    check_sign["text"] = "✔" * (4 if reps > 0 and reps % 8 == 0 else completed)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    global timer
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer = None
        next_session()

# ---------------------------- UI SETUP ------------------------------- #

#The Timer Window
window = tk.Tk()
window.title("Pomodoro")
#The Timer Text
window.config(padx=120, pady=50, bg=YELLOW)
label = tk.Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 40))
label.grid(row=0, column=1)

#The Image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file=str(Path(__file__).resolve().parent / "tomato.png"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#The Start Button
start_button = tk.Button(text="Start", bg="white", command=start_timer)
start_button.grid(row=2, column=0)

#The Reset Button
reset_button = tk.Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(row=2, column=2)

#The CheckBox
check_sign = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
check_sign.grid(row=3, column=1)



window.mainloop()
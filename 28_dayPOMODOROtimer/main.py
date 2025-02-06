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
LONG_BREAK_MIN = 20
repeat = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_label.config(text="")
    global repeat
    repeat = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repeat
    repeat += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repeat == 1:  # Ensure the first session is always work
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)
    elif repeat % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif repeat % 2 == 0:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)
    else:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)

    
    




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" 
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(repeat/2)
        for _ in range(work_session):
            mark += "✔"
        check_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

window.after(1000, )

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

my_label = Label(text="Timer", font=("Arial", 25, "bold"), bg=YELLOW)
my_label.grid(column=1, row=0)

buttonStart = Button(text="Start", command=start_timer)
buttonStart.grid(column=0, row=2)

buttonReset = Button(text="Reset", command=reset_timer)
buttonReset.grid(column=2, row=2)

check_label = Label(bg=YELLOW)
check_label.grid(column=1, row=2)








window.mainloop()

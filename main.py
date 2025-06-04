from tkinter import Tk, ttk, PhotoImage, StringVar, IntVar
from random import randint


def check_win(param):
    # 0 - камень, 1 - ножницы, 2 - бумага
    # выигрыши:  0-1, 2-0, 1-2
    # проигрыши: 1-0, 0-2, 2-1
    computer = computer_choice.get()
    if param == computer:
        text.set("Ничья!")
    elif (param == 0 and computer == 1) or (param == 2 and computer == 0) or (param == 1 and computer == 2):
        text.set("Ты выиграл!")
        your_balls.set(your_balls.get() + 1)
    else:
        text.set("Ты проиграл!")
        computer_balls.set(computer_balls.get() + 1)

    match computer:
        case 0:
            label11.configure(image=image_rock)
            label11.image = image_rock
        case 1:
            label11.configure(image=image_scissors)
            label11.image = image_scissors
        case 2:
            label11.configure(image=image_paper)
            label11.image = image_paper
        case _:
            label11.configure(image=image_start)
            label11.image = image_start

    button21.configure(state="disabled")
    button22.configure(state="disabled")
    button23.configure(state="disabled")

    if your_balls == 1000:
        text.set("ОЧЕНЬ ДАЖЕ НЕПЛОХО!")

    root.after(1000, new_step)

def new_step():
    computer_choice.set(randint(0, 2))
    label11.configure(image=image_start)
    label11.image = image_start
    button21.configure(state="normal")
    button22.configure(state="normal")
    button23.configure(state="normal")

root = Tk()
root.geometry("400x400+600+200")
root.title("Камень-ножницы-бумага")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure(style="My.TLabel", font=("Lucida Sans Unicode", 12))

# Переменные
your_balls = IntVar()
computer_balls = IntVar()
text = StringVar(value="Начнем игру!")
computer_choice = IntVar(value=randint(0, 2))
image_start = PhotoImage(file="images/start.png")
image_rock = PhotoImage(file="images/rock.png")
image_scissors = PhotoImage(file="images/scissors.png")
image_paper = PhotoImage(file="images/paper.png")
image_rock1 = PhotoImage(file="images/rock1.png")
image_scissors1 = PhotoImage(file="images/scissors1.png")
image_paper1 = PhotoImage(file="images/paper1.png")

#  Определяем frames
frame1 = ttk.Frame(root, relief="raised")
frame1.place(relx=0.5, relwidth=0.9, rely=0.25, relheight=0.4, anchor="center")
frame2 = ttk.Frame(root)
frame2.place(relx=0.5, relwidth=0.9, rely=0.65, relheight=0.3, anchor="center")
frame3 = ttk.Frame(root, relief="groove")
frame3.place(relx=0.5, relwidth=0.9, rely=0.9, relheight=0.1, anchor="center")

# Заполняем frame1
for r in range(2): frame1.rowconfigure(index=r, weight=1)
for c in range(3): frame1.columnconfigure(index=c, weight=1)
label11 = ttk.Label(frame1, image=image_start, anchor="center")
label11.grid(row=0, column=1, rowspan=2, sticky="nsew")
label12 = ttk.Label(frame1, text="Ваши \nбаллы", anchor="center", background="#B4CBFC", style="My.TLabel")
label12.grid(row=0, column=0, sticky="nsew")
label13 = ttk.Label(frame1, text="Его \nбаллы", anchor="center", background="#B4CBFC", style="My.TLabel")
label13.grid(row=0, column=2, sticky="nsew")
label14 = ttk.Label(frame1, textvariable=your_balls, anchor="center", style="My.TLabel")
label14.grid(row=1, column=0, sticky="n")
label15 = ttk.Label(frame1, textvariable=computer_balls, anchor="center", style="My.TLabel")
label15.grid(row=1, column=2, sticky="n")

# Заполняем frame2
for r in range(1): frame2.rowconfigure(index=r, weight=1)
for c in range(3): frame2.columnconfigure(index=c, weight=1)
button21 = ttk.Button(frame2, image=image_rock1, command=lambda: check_win(0))
button21.grid(row=0, column=0)
button22 = ttk.Button(frame2, image=image_scissors1, command=lambda: check_win(1))
button22.grid(row=0, column=1)
button23 = ttk.Button(frame2, image=image_paper1, command=lambda: check_win(2))
button23.grid(row=0, column=2)

# Заполняем frame3
label3 = ttk.Label(frame3, textvariable=text, anchor="center", style="My.TLabel")
label3.place(relx=0.5, rely=0.5, anchor="center")


root.mainloop()
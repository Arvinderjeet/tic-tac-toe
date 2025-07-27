from tkinter import *
import tkinter as tk
import random

root = Tk()
root.title("Tic-Tac-Toc")
root.geometry('520x570')

turn_label = Label(root, text = "", font=("Arial", 20), fg="blue", bg="white", bd=2, relief="ridge")
win_label = Label(root, text = "", font=("Arial", 20), fg="red", bd=0, relief="ridge")

def set_default():
    global mat_table
    global current
    mat_table = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
    current = random.choice(["O","X"])
    turn_label.configure(text = f"Turn: {current}")
    win_label.config(bd=0, text="")

def toggle_turn(curr):
    global current
    current = "X" if curr == "O" else "O"

def check_draw():
    for row in mat_table:
        if "   " in row:
            return False
    return True

def is_valid(row, col):
    if 0 <= row < 3 and 0 <= col < 3:
        if mat_table[row][col] == "   ":
            return True
    return False

def is_won():
    for i in range(3):
        if "".join(mat_table[i]) in ['XXX', 'OOO']:
            return True

    # COLS
    for i in range(3):
        if "".join([mat_table[0][i],mat_table[1][i],mat_table[2][i]]) in ['XXX', 'OOO']:
            return True

    # DIAGONALS
    if "".join([mat_table[0][0],mat_table[1][1],mat_table[2][2]]) in ['XXX', 'OOO']:
        return True
    if "".join([mat_table[0][2],mat_table[1][1],mat_table[2][0]]) in ['XXX', 'OOO']:
        return True
    return False

def update(row, col, current):
    print(current, row, col)

    if is_valid(row, col):
        mat_table[row][col] = current
        toggle_turn(current)
        print("whose turn", current)
        if check_draw():
            win_label.config(bd=3, text="It's a DRAW !!!", fg="orange")
            display()
            disable_buttons()
            print("It's a DRAW !!!")
            root.after(3000, lambda: [set_default(), display()])
        elif is_won():
            win_label.config(bd=3, text=f"{current} WON !!!".format(current = current), fg="green")
            display()
            disable_buttons()
            print(f"{current} won!".format(current=current))
            root.after(3000, lambda: [set_default(), display()])
        else:
            display()
            win_label.configure(text="", bd = 0)
        print(mat_table)
    else:
        win_label.config(bd=2, text = "invalid move, try again", fg="red")

def display_button():
    turn_label.configure(text=f"Turn: {current}")
    global r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3

    r1c1 = tk.Button(root, text=mat_table[0][0], command=lambda: update(0, 0, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r1c2 = tk.Button(root, text=mat_table[0][1], command=lambda: update(0, 1, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r1c3 = tk.Button(root, text=mat_table[0][2], command=lambda: update(0, 2, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r2c1 = tk.Button(root, text=mat_table[1][0], command=lambda: update(1, 0, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r2c2 = tk.Button(root, text=mat_table[1][1], command=lambda: update(1, 1, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r2c3 = tk.Button(root, text=mat_table[1][2], command=lambda: update(1, 2, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r3c1 = tk.Button(root, text=mat_table[2][0], command=lambda: update(2, 0, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r3c2 = tk.Button(root, text=mat_table[2][1], command=lambda: update(2, 1, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )
    r3c3 = tk.Button(root, text=mat_table[2][2], command=lambda: update(2, 2, current), activebackground="blue",
                       anchor="center", bd=20, cursor="hand2", font=("Arial", 30), highlightthickness=2, justify="center" )

    r1c1.place(x=100, y=120)
    r1c2.place(x=200, y=120)
    r1c3.place(x=300, y=120)
    r2c1.place(x=100, y=240)
    r2c2.place(x=200, y=240)
    r2c3.place(x=300, y=240)
    r3c1.place(x=100, y=360)
    r3c2.place(x=200, y=360)
    r3c3.place(x=300, y=360)

def disable_buttons():
    global r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3
    r1c1.config(state="disabled")
    r1c2.config(state="disabled")
    r1c3.config(state="disabled")
    r2c1.config(state="disabled")
    r2c2.config(state="disabled")
    r2c3.config(state="disabled")
    r3c1.config(state="disabled")
    r3c2.config(state="disabled")
    r3c3.config(state="disabled")

def get_turn():
    global current
    print("turn : {current}".format(current=current))

def display():
    display_button() # Yes, I know this function does only one task: calling another function... it looks nice to me :D

set_default()
display()

turn_label.pack()
win_label.pack()
root.mainloop()

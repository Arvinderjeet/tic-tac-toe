from tkinter import *
import tkinter as tk
import random

root = Tk()
root.title("Tic-Tac-Toc")
root.geometry('520x570')

a = Label(root, text = "Turn: [X/o]")

def set_default():
    global mat_table
    global current
    mat_table = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
    current = random.choice(["O","X"])

def is_valid(row, col):
    # TODO: add validation
    return True

def is_won():
    win_state = False
    # TODO: check winning state and return true
    return win_state

def update(row, col, current):
    if is_valid(row, col):
        mat_table[row][col] = current
        if is_won():# TODO: prompt who won with buttons(retry/ give-up)
            pass
    else:
        print("position already taken or dont exist")
def button_clicked():
    print("Button clicked!")

def icon(row):
    return mat_table[row-1]

def display_buttons(row = 1):
    current_row = icon(row)
    for i in range(1,4):
        button = tk.Button(root,
                text=current_row[i-1],
                command= lambda: update(row-1, i, current_row[i-1]),
                activebackground="blue",
                anchor="center",
                bd=20,
                cursor="hand2",
                font=("Arial", 30),
                highlightthickness=2,
                justify="center"
        )
        button.place(x=100 * i, y=120 * row)


def get_turn():
    global current
    print("turn : {current}".format(current=current))

def display():
    for i in range(3):
        display_buttons(i + 1)
    get_turn()

set_default()
display()



a.pack()
root.mainloop()

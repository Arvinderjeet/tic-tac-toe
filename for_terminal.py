import os
import random

# mat_table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
# current = random.choice(["O","X"])


def set_default():
    global mat_table
    global current
    mat_table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    current = random.choice(["O","X"])

def is_won(rc):
    # ROWS
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

    global current
    current = "X" if current == "O" else "O"
    return False

def is_valid(r, c):
    if 0 < r <= 3 and 0 < c <= 3:
        if mat_table[r-1][c-1] == "-":
            return True
    return False

def update(r, c, who) -> None:
    mat_table[r-1][c-1] = who

def get_turn():
    global current
    print("turn : {current}".format(current=current))

    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if is_valid(row, col):
            update(row, col, current)
            if is_won(mat_table):
                print(f"{current} won!".format(current=current))
                for i in mat_table:
                    print(*i)
                print("RETRY (Y/N): ")
                inp = input()
                if inp.lower() == "y":
                    set_default()
                    break
                else:
                    exit(0)
            break
        else:
            print("position already taken or dont exist")
    display()

def display():
    os.system("cls")
    print()
    for i in mat_table:
        print(*i)

    print()
    get_turn()

set_default()
display()
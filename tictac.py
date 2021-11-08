from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

# Disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


#Check if someone won
def checkifwon():
    global winner, player, l1, turnUI
    winner = False

    if turn == '0':
        player = 'O'
    else:
        player = '0'

    if b1["text"] == b2["text"] == b3["text"] != " ":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()
    elif b4["text"] == b5["text"] == b6["text"] != " ":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()
    elif b7["text"] == b8["text"] == b9["text"] != " ":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()
    elif b1["text"] == b4["text"] == b7["text"] != " ":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()
    elif b2["text"] == b5["text"] == b8["text"] != " ":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()
    elif b3["text"] == b6["text"] == b9["text"] != " ":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()
    elif b1["text"] == b5["text"] == b9["text"] != " ":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()
    elif b3["text"] == b5["text"] == b7["text"] != " ":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", player +" Wins")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe", "      It's a tie!\nStart a new game")
        winner = True
        disable_all_buttons()

    elif winner != True:
        turnUI = "Player: " + turn
        l1 = Label(root, text=turnUI, height=3, font=("Helvetica", 10, "bold"), bg="SystemButtonFace")
        l1.grid(row=0, column=1)


#Button click function
def b_click(b):
    global turn, count

    if b["text"] == " " and turn == '0':
        b["text"] = "0"
        turn = 'O'
        count += 1
        checkifwon()
    elif b["text"] == " " and turn == 'O':
        b["text"] = "O"
        turn = '0'
        count += 1
        checkifwon()


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, l1, test
    global count, turn
    count = 0
    turn = '0'

    turnUI = "Player: " + turn
    l1 = Label(root, text=turnUI, height=3, font=("Helvetica", 10, "bold"), bg="SystemButtonFace")

    # Build Button
    b0 = Button(root, text="New Game", font=("Helvetica", 10), height=3, bg="SystemButtonFace", command=reset)

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    l1.grid(row=0, column=1)
    b0.grid(row=0, column=2)

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)
    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)
    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)


reset()
root.mainloop()

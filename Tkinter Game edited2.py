from tkinter import *
from tkinter import messagebox
from tkinter import tkFileDialog


root = Tk()
root.title('Tic-Tac-Slide')

# X starts so true
clicked = True
count = 0

# disable all the buttons
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
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    # b17.config(state=DISABLED)

# Check to see if someone won
def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X" and b4["text"]  == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        b4.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b5["text"] == "X" and b6["text"] == "X" and b7["text"]  == "X" and b8["text"]  == "X":
        b5.config(bg="red")
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b9["text"] == "X" and b10["text"] == "X" and b11["text"]  == "X" and b12["text"]  == "X":
        b9.config(bg="red")
        b10.config(bg="red")
        b11.config(bg="red")
        b12.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b13["text"] == "X" and b14["text"] == "X" and b15["text"]  == "X" and b16["text"]  == "X":
        b13.config(bg="red")
        b14.config(bg="red")
        b15.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X" and b13["text"]  == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b2["text"] == "X" and b6["text"] == "X" and b10["text"]  == "X" and b14["text"]  == "X":
        b2.config(bg="red")
        b6.config(bg="red")
        b10.config(bg="red")
        b14.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b7["text"] == "X" and b11["text"]  == "X" and b15["text"]  == "X":
        b3.config(bg="red")
        b7.config(bg="red")
        b11.config(bg="red")
        b15.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b4["text"] == "X" and b8["text"] == "X" and b12["text"]  == "X" and b16["text"]  == "X":
        b4.config(bg="red")
        b8.config(bg="red")
        b12.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b6["text"] == "X" and b11["text"]  == "X" and b16["text"]  == "X":
        b1.config(bg="red")
        b6.config(bg="red")
        b11.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b4["text"] == "X" and b7["text"] == "X" and b10["text"]  == "X" and b13["text"]  == "X":
        b4.config(bg="red")
        b7.config(bg="red")
        b10.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    #### CHECK FOR O's Win
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O" and b4["text"]  == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        b4.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b5["text"] == "O" and b6["text"] == "O" and b7["text"]  == "O" and b8["text"]  == "O":
        b5.config(bg="red")
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b9["text"] == "O" and b10["text"] == "O" and b11["text"]  == "O" and b12["text"]  == "O":
        b9.config(bg="red")
        b10.config(bg="red")
        b11.config(bg="red")
        b12.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b13["text"] == "O" and b14["text"] == "O" and b15["text"]  == "O" and b16["text"]  == "O":
        b13.config(bg="red")
        b14.config(bg="red")
        b15.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O" and b13["text"]  == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b2["text"] == "O" and b6["text"] == "O" and b10["text"]  == "O" and b14["text"]  == "O":
        b2.config(bg="red")
        b6.config(bg="red")
        b10.config(bg="red")
        b14.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b7["text"] == "O" and b11["text"]  == "O" and b15["text"]  == "O":
        b3.config(bg="red")
        b7.config(bg="red")
        b11.config(bg="red")
        b15.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b4["text"] == "O" and b8["text"] == "O" and b12["text"]  == "O" and b16["text"]  == "O":
        b4.config(bg="red")
        b8.config(bg="red")
        b12.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b6["text"] == "O" and b11["text"]  == "O" and b16["text"]  == "O":
        b1.config(bg="red")
        b6.config(bg="red")
        b11.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b4["text"] == "O" and b7["text"] == "O" and b10["text"]  == "O" and b13["text"]  == "O":
        b4.config(bg="red")
        b7.config(bg="red")
        b10.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    # Check if tie
    if count == 16 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
        disable_all_buttons()
                
# Button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Dammit Joe.. that box has already been selected\nPick Another Box..." )

# A shift of the turned tiles to the left

def shiftleft():
    
    global clicked, count
    # if direction == "left":
    if b1["text"] != " ":
        count = count-1
    b1["text"] = b2["text"]
    b2["text"] = b3["text"]
    b3["text"] = b4["text"]
    b4["text"] = " "
    if b5["text"] != " ":    
         count = count-1
    b5["text"] = b6["text"]
    b6["text"] = b7["text"]
    b7["text"] = b8["text"]
    b8["text"] = " "
    if b9["text"] != " ":
        count = count-1
    b9["text"] = b10["text"]
    b10["text"] = b11["text"]
    b11["text"] = b12["text"]
    b12["text"] = " "
    if b13["text"] != " ":
        count = count-1
    b13["text"] = b14["text"]
    b14["text"] = b15["text"]
    b15["text"] = b16["text"]
    b16["text"] = " "
    print(count)

        
def shiftright():
    
    global clicked, count
    
    if b4["text"] != " ":
        count = count-1
    b4["text"] = b3["text"]
    b3["text"] = b2["text"]
    b2["text"] = b1["text"]
    b1["text"] = " "
    
    if b8["text"] != " ":    
         count = count-1
    b8["text"] = b7["text"]
    b7["text"] = b6["text"]
    b6["text"] = b5["text"]
    b5["text"] = " "
    
    if b12["text"] != " ":
        count = count-1
    b12["text"] = b11["text"]
    b11["text"] = b10["text"]
    b10["text"] = b9["text"]
    b9["text"] = " "
    
    if b16["text"] != " ":
        count = count-1
    b16["text"] = b15["text"]
    b15["text"] = b14["text"]
    b14["text"] = b13["text"]
    b13["text"] = " "
    print(count)

    
def shifttop():
    
    global clicked, count
    
    if b1["text"] != " ":
        count = count-1
    b1["text"] = b5["text"]
    b5["text"] = b9["text"]
    b9["text"] = b13["text"]
    b13["text"] = " "
    if b2["text"] != " ":    
         count = count-1
    b2["text"] = b6["text"]
    b6["text"] = b10["text"]
    b10["text"] = b14["text"]
    b14["text"] = " "
    if b3["text"] != " ":
        count = count-1
    b3["text"] = b7["text"]
    b7["text"] = b11["text"]
    b11["text"] = b15["text"]
    b15["text"] = " "
    if b4["text"] != " ":
        count = count-1
    b4["text"] = b8["text"]
    b8["text"] = b12["text"]
    b12["text"] = b16["text"]
    b16["text"] = " "
    print(count)
    
    
def shiftdown():
    
    global clicked, count
    
    if b13["text"] != " ":
        count = count-1
    b13["text"] = b9["text"]
    b9["text"] = b5["text"]
    b5["text"] = b1["text"]
    b1["text"] = " "
    if b14["text"] != " ":    
         count = count-1
    b14["text"] = b10["text"]
    b10["text"] = b6["text"]
    b6["text"] = b2["text"]
    b2["text"] = " "
    if b15["text"] != " ":
        count = count-1
    b15["text"] = b11["text"]
    b11["text"] = b7["text"]
    b7["text"] = b3["text"]
    b3["text"] = " "
    if b16["text"] != " ":
        count = count-1
    b16["text"] = b12["text"]
    b12["text"] = b8["text"]
    b8["text"] = b4["text"]
    b4["text"] = " "
    print(count)


def bottomright():
    shiftright()
    shiftdown()
    

def bottomleft():
    shiftdown()
    shiftleft()
    
def topleft():
    shifttop()
    shiftleft()
    
def topright():
    shifttop()
    shiftright()    
   
    
    
    
def shiftbr():
    print("Shift break")
    
# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16
    global clicked, count
    clicked = True
    count = 0

    # Build our buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
    b10 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b10))
    b11 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b11))
    b12 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b12))
    
    b13 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b13))
    b14 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b14))
    b15 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b15))
    b16 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b16))

    # b17 = Button(root, text="Shift", font=("Helvetica", 20), height=3, width=3, bg="SystemButtonFace", command=lambda: b_click(b17))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)

    b5.grid(row=1, column=0)
    b6.grid(row=1, column=1)
    b7.grid(row=1, column=2)
    b8.grid(row=1, column=3)

    b9.grid(row=2, column=0)
    b10.grid(row=2, column=1)
    b11.grid(row=2, column=2)
    b12.grid(row=2, column=3)

    b13.grid(row=3, column=0)
    b14.grid(row=3, column=1)
    b15.grid(row=3, column=2)
    b16.grid(row=3, column=3)

    

    # b1.grid(row=0, column=0)
    # b2.grid(row=0, column=1)
    # b3.grid(row=0, column=2)
    # b4.grid(row=0, column=3)

    # b5.grid(row=1, column=0)
    # b6.grid(row=1, column=1)
    # b7.grid(row=1, column=2)
    # b8.grid(row=1, column=3)

    # b9.grid(row=2, column=0)
    # b10.grid(row=2, column=1)
    # b11.grid(row=2, column=2)
    # b12.grid(row=2, column=3)

    # b13.grid(row=3, column=0)
    # b14.grid(row=3, column=1)
    # b15.grid(row=3, column=2)
    # b16.grid(row=3, column=3)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
shift_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

my_menu.add_cascade(label="Shift", menu=shift_menu)
shift_menu.add_command(label="Shift Left", command=shiftleft)
shift_menu.add_command(label="Shift Right", command=shiftright)
shift_menu.add_command(label="Shift Up", command=shifttop)
shift_menu.add_command(label="Shift Down", command=shiftdown)

shift_menu.add_command(label="Shift Top Left", command=topleft)
shift_menu.add_command(label="Shift Bottom Left", command=bottomleft)
shift_menu.add_command(label="Shift Top Right", command=topright)
shift_menu.add_command(label="Shift Bottom Right", command=bottomright)

reset()


root.mainloop()

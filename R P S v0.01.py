#Task 1, Make a frame for the game.
#Task 2, The computer makes its choice randomly, and the game continues until the user decides to quit.
#Task 3, write a Python program that lets you play Rock, Paper, Scissors against the computer. 
#Task 4 , add images of the rock paper and scissors to each button.

import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk #Import PIL library for images

def play(user):
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        result = "It's a tie!"
    elif is_win(user, computer):
        result = "You won!"
    else:
        result = "You lost!"
    messagebox.showinfo("Result",result)


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
	
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def create_gui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    label = tk.Label(root, text="Choose your move:")
    label.pack(pady=10)

    #Load Images
    rock_img = ImageTk.PhotoImage(Image.open("R.JPG").resize((50,50)))
    paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((50,50)))
    scissors_img = ImageTk.PhotoImage(Image.open("scissors.jpg").resize((50,50)))

    #buttons_with_image
    rock_button = tk.Button(root, text="Rock", command=lambda: play ('r'))
    rock_button.image_names = rock_img
    rock_button.pack(pady=5)
    

    paper_button = tk.Button(root, text="paper", command=lambda: play ('p'))
    paper_button.pack(pady=5)

    scissors_button = tk.Button(root, text="scissors", command=lambda: play('s'))
    scissors_button.pack(padx=5)

    quit_button = tk.Button(root, text='quit', command=root.quit)
    quit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()

#This code defines two functions: play and is_win. 
#The play function takes the user’s input and generates the computer’s choice using the random.choice function

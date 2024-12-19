import tkinter as tk
import random

def determine_winner(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors Game")

computer_label = tk.Label(root, text="Computer chose: ")
computer_label.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"))
paper_button.pack(side=tk.LEFT, padx=20)

scissors_button = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=20)

# Run the application
root.mainloop()

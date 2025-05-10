import tkinter as tk
import game_Moudle as game

def menu():
    root = tk.Tk()
    root.title("Random Questions Game")
    WelcomeLabel = tk.Label(root, text="Welcome to the random questions game!", font=("Arial", 15))
    WelcomeLabel.pack(padx=20, pady=20)
    PlayButton = tk.Button(root, text="Play", font=("Arial", 15), command=lambda: game.Question1(root))
    PlayButton.pack()
    root.geometry("400x500")
    root.mainloop()

menu()
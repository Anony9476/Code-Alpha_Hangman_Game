import tkinter as tk
import random
from tkinter import messagebox

def new_game():
    global word, guessed_letters, attempts
    words = ['python', 'developer', 'hangman', 'programming', 'algorithm', 'beginner', 'learning', 'simple']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    update_display()

def update_display():
    display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    word_label.config(text=display_word)
    attempts_label.config(text=f"Attempts left: {attempts}")
    guessed_label.config(text=f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None yet'}")

def guess_letter(letter):
    global attempts
    if letter in guessed_letters:
        messagebox.showinfo("Info", "You've already guessed that letter!")
        return
    
    guessed_letters.add(letter)
    if letter not in word:
        attempts -= 1
    update_display()
    check_game_status()

def check_game_status():
    if set(word) == guessed_letters:
        messagebox.showinfo("Victory!", f"🎉 You revealed the magic word: {word}")
        new_game()
    elif attempts == 0:
        messagebox.showinfo("Game Over", f"💀 The magic word was: {word}")
        new_game()

# Initialize Tkinter window
root = tk.Tk()
root.title("Mystery Hangman")
root.geometry("400x500")
root.resizable(False, False)

# UI Elements
word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=20)

attempts_label = tk.Label(root, text="", font=("Arial", 14))
attempts_label.pack()

guessed_label = tk.Label(root, text="", font=("Arial", 12))
guessed_label.pack()

frame = tk.Frame(root)
frame.pack()

for i in range(26):
    letter = chr(65 + i).lower()
    btn = tk.Button(frame, text=letter, width=4, height=2, font=("Arial", 12), 
                     command=lambda l=letter: guess_letter(l))
    btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)

new_game_btn = tk.Button(root, text="New Game", font=("Arial", 14), command=new_game)
new_game_btn.pack(pady=10)

# Start a new game initially
new_game()

# Run Tkinter event loop
root.mainloop()

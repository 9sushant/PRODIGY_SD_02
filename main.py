import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x200")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
                self.submit_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
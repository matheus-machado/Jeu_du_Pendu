import tkinter as tk

class ZoneAffichage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#c0d9e2")

        self.boutons = []  # Initialize list of buttons

        # Create buttons for each letter of the alphabet
        for i in range(26):
            letter = chr(ord('A') + i)  # Convert index to corresponding letter
            button = tk.Button(self, text=letter)
            button.grid(row=i//7, column=i%7, padx=1, pady=1)  # Position button in a 6x5 grid
            self.boutons.append(button)  # Add button to list
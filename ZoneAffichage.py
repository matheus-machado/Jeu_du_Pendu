import tkinter as tk
from formes import *
class ZoneAffichage(tk.Frame):
    def __init__(self, can):
        super().__init__( bg="#c0d9e2")
        # Base, Poteau, Traverse, Corde
        
        self.base = [Rectangle(120,  350, 140,  12, "white"), Rectangle(115,  220,  12, 260, "white"), Rectangle(164, 90, 110,  12, "white"), Rectangle(214,  110,  10,  40, "white")]

        
        
        
        
        self.bonhomme_list = [Rectangle(213, 140,  40,  40, "black"), Rectangle(213, 190,  26,  80, "black"), Rectangle(178, 170,  47,  10, "black"), Rectangle(248, 170,  47,  10, "black"), Rectangle(205, 250,  10,  40, "black"), Rectangle(221, 250,  10,  40, "black")]

        # # Tete, Tronc
        # Rectangle(213, 140,  40,  40, "black").affiche(can)
        # Rectangle(213, 190,  26,  80, "black").affiche(can)
        # # Bras gauche et droit
        # Rectangle(178, 170,  47,  10, "black").affiche(can)
        # Rectangle(248, 170,  47,  10, "black").affiche(can)
        # # Jambes gauche et droite
        # Rectangle(205, 250,  10,  40, "black").affiche(can)
        # Rectangle(221, 250,  10,  40, "black").affiche(can)

        # self.boutons = []  # Initialize list of buttons

        # # Create buttons for each letter of the alphabet
        # for i in range(26):
        #     letter = chr(ord('A') + i)  # Convert index to corresponding letter
        #     button = tk.Button(text=letter)
        #     button.grid(row=i//7, column=i%7, padx=1, pady=1)  # Position button in a 6x5 grid
        #     self.boutons.append(button)  # Add button to list
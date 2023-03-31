import tkinter as tk
from ZoneAffichage import ZoneAffichage
import random

class FenPrincipale(tk.Tk):
    def __init__(self):
        super().__init__()



        self.title("Clavier virtuel")
        self.geometry("500x550")  

        self.configure(bg="#c0d9e2")

        self.zone_affichage = ZoneAffichage(self)
        self.zone_affichage.place(relx=0.5, rely=0.7, anchor=tk.N)
        
        self.bouton_quitter = tk.Button(self, text="Quitter", command=self.quitter)
        self.bouton_quitter.pack(side=tk.TOP, padx=10, pady=10)
        
        self.bouton_nouvelle_partie = tk.Button(self, text="Nouvelle partie", command=self.nouvelle_partie)
        self.bouton_nouvelle_partie.pack( side = tk.TOP, pady=10)
        
        self.boutons = []
        for i in range(26):
            lettre = chr(ord('A')+i)
            bouton = tk.Button(self.zone_affichage,  text=lettre, state=tk.DISABLED)
            bouton.grid(row=i//7, column=i%7, padx=5, pady=5, sticky="nsew")  # Use a Grid layout manager
            self.boutons.append(bouton)




        self.zone_dessin = tk.Canvas(self, width=200, height=200, bg="white",insertborderwidth=10)
        self.zone_dessin.pack(pady=10)

        self.__mots = self.charger_mots()

        self.mot_a_deviner = tk.StringVar()
        self.mot_a_deviner.set("")
        self.label_mot = tk.Label(self, textvariable=self.mot_a_deviner, font=("Courier", 16))
        self.label_mot.pack(pady=10)




    def charger_mots(self):
        mots = []
        with open("mots.txt", "r") as f:
            for ligne in f:
                mots.append(ligne.strip())
        return mots

    def nouvelle_partie(self):
        mot = random.choice(self.__mots)
        self.mot_a_deviner.set(mot)
        for bouton in self.boutons:
            bouton.config(state=tk.NORMAL)
        self.zone_dessin.delete("all")

    def quitter(self):
        self.destroy()


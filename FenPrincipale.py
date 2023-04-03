import tkinter as tk
from ZoneAffichage import ZoneAffichage
import random

class FenPrincipale(tk.Tk):
    def __init__(self):
        super().__init__()



        self.title("Clavier virtuel")
        self.geometry("600x900")  

        self.configure(bg="#c0d9e2")

        

        self.bouton_quitter = tk.Button(self, text="Quitter", command=self.quitter)
        self.bouton_quitter.pack(side=tk.TOP, padx=10, pady=10)
        
        self.bouton_nouvelle_partie = tk.Button(self, text="Nouvelle partie", command=self.nouvelle_partie)
        self.bouton_nouvelle_partie.pack( side = tk.TOP, pady=10)
        
        self.mot_a_deviner = tk.StringVar()
        self.motActuel = tk.StringVar()
        self.mot_a_deviner.set("")
        self.motActuel.set("START A NEW GAME")
        self.label_mot = tk.Label(self, textvariable=self.motActuel, font=("Courier", 16), bg="#c0d9e2")
        self.label_mot.pack(pady=10)
        self.coupsRestants = 10
        self.lettresJouees = []        
        
        def cliquer(self):
            self.config(state=tk.DISABLED)
            self.traitement(self.lettre)
        


        # self.bouton= tk.Button( self, text=lettre,  command = self.cliquer, state=tk.DISABLED)
        # self.bouton.pack( side = tk.TOP, pady=10)
       
        self.zone_dessin = tk.Canvas(self, width=400, height=400, bg = '#f7a156')
        self.zone_dessin.pack(pady=10)

        self.zone_affichage = ZoneAffichage(self.zone_dessin)
        self.zone_affichage.place(relx=0.5, rely=0.7, anchor=tk.N)  

        for i in range(4):
            self.zone_affichage.base[i].affiche(self.zone_dessin)


        self.boutons = []

        for i in range(26):
            lettre = chr(ord('A')+i)
            bouton= tk.Button( self.zone_affichage, text=lettre,  command = lambda index =i: self.cliquer(index), state=tk.DISABLED)
            #bouton = tk.Button(self.zone_affichage,  text=lettre, command= self.cliquer(), state=tk.DISABLED)
            bouton.grid(row=i//7, column=i%7, padx=5, pady=5, sticky="nsew", ipadx=20, ipady=15)  # Use a Grid layout manager
            self.boutons.append(bouton)
        
        self.etatPartie = tk.StringVar()
        self.etatPartie.set("Vous avez " + str(self.coupsRestants) + ' coups restants')
        self.label_etatPartie= tk.Label(self, textvariable=self.etatPartie, font=("Courier", 16), bg="#c0d9e2")
        self.label_etatPartie.pack(pady=10)

        self.__mots = self.charger_mots()

    def cliquer(self, index):
        self.boutons[index].config(state=tk.DISABLED)
        lettre = self.boutons[index]['text']
        self.traitement(lettre)

    def charger_mots(self):
        mots = []
        with open("mots.txt", "r") as f:
            for ligne in f:
                mots.append(ligne.strip())
        return mots

    def nouvelle_partie(self):
        self.coupsRestants = 10
        self.etatPartie.set("Vous avez " + str(self.coupsRestants) + ' coups restants')


        

        mot = random.choice(self.__mots)
        self.mot_a_deviner.set(mot)
        self.motActuel.set(len(mot)*'*')
        self.label_mot = tk.Label(self, textvariable=self.motActuel, font=("Courier", 16))

        for bouton in self.boutons:
             bouton.config(state=tk.NORMAL)
        self.zone_dessin.delete("all")

        for i in range(4):
            self.zone_affichage.base[i].affiche(self.zone_dessin)

    def quitter(self):
        self.destroy()

    def traitement(self, lettre):

        if self.mot_a_deviner is None:
            return
        
        mot = self.mot_a_deviner.get()
        self.lettresJouees.append(lettre)
        
        if lettre not in (mot):
            self.coupsRestants -= 1
            self.etatPartie.set("Vous avez " + str(self.coupsRestants) + ' coups restants')

            
        for i in range(len(mot)):
            if str(mot)[i] == lettre:
                copy_to_str = list(str(self.motActuel.get()))
                copy_to_str[i]=lettre
                lettreReveal = "".join(copy_to_str)
                self.motActuel.set(lettreReveal)
        
        print(self.coupsRestants)
        if self.coupsRestants == 9:
            print('cabeca')
            self.zone_affichage.bonhomme_list[0].affiche(self.zone_dessin)
        elif self.coupsRestants == 7:
            self.zone_affichage.bonhomme_list[1].affiche(self.zone_dessin)
        elif self.coupsRestants == 5:
            self.zone_affichage.bonhomme_list[2].affiche(self.zone_dessin)
        elif self.coupsRestants == 3:
            self.zone_affichage.bonhomme_list[3].affiche(self.zone_dessin)
        elif self.coupsRestants == 2:
            self.zone_affichage.bonhomme_list[4].affiche(self.zone_dessin) 
        elif self.coupsRestants == 0:
            self.zone_affichage.bonhomme_list[5].affiche(self.zone_dessin) 
            
            



        # self.afficherMot()
        print(str(self.motActuel.get()))
        print(str(mot))
        if str(self.motActuel.get()) == str(mot):
            for bouton in self.boutons:
                bouton.config(state=tk.DISABLED)
            print("Vous avez gagné !")
            self.etatPartie.set("Vous avez gagné !")
        elif self.coupsRestants <= 0:
            for bouton in self.boutons:
                bouton.config(state=tk.DISABLED)
            self.etatPartie.set("Vous avez perdu !")
            print("Vous avez perdu !")

# class Button(FenPrincipale):
#         def __init__(self):
#             self.boutons = []
#             for i in range(26):
#                 lettre = chr(ord('A')+i)
#                 bouton= tk.Button( self.zone_affichage, text=lettre,  state=tk.DISABLED)
#                 #bouton = tk.Button(self.zone_affichage,  text=lettre, command= self.cliquer(), state=tk.DISABLED)
#                 bouton.grid(row=i//7, column=i%7, padx=5, pady=5, sticky="nsew")  # Use a Grid layout manager
#                 self.button.append(bouton)
                
# class MonBoutonLettre(tk.Button):
    
#     def __init__(self,  lettre):
#         self = tk.Button(self.zone_affichage,  text=lettre, command= self.cliquer(), state=tk.DISABLED)
#         self.lettre = lettre
        
    
#     def cliquer(self):
#         self.config(state=tk.DISABLED)
#         FenPrincipale.traitement(self.lettre)
#         print('oiii cliquei')


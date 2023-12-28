import tkinter as tk
from tkinter import messagebox
import random

class JeuDuPendu:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Pendu")

        # Liste de mots
        self.liste_de_mots = [
            "PYTHON",
            "JAVA",
            "JAVASCRIPT",
            "HTML",
            "CSS",
            "RUBY",
            "C",
            "DEVELOPPEMENT",
            "PROGRAMMATION",
            "GITHUB",
            "INTERFACE",
            "OPENAI",
            "INTELLIGENCE",
            "APPRENTISSAGE",
            "PYTHONIQUE",
            "RESEAUX",
            "BASESDEDONNEES",
            "ANALYSE",
            "VISUALISATION",
            "ALGORITHME",
            "STRUCTURESDEDONNEES",
            "OPTIMISATION",
            "SECURITE",
            "CRYPTOGRAPHIE",
            "LANGAGENATUREL",
            "MACHINELEARNING",
            "NEURALNETWORK",
            "SYNTHETICDATA",
            "AUTOMATION",
            "ROBOTIQUE",
            "INTERNETOFTHINGS",
            "BLOCKCHAIN",
            "CLOUDCOMPUTING",
            "DOCKER",
            "KUBERNETES",
            "MICROSERVICES",
            "WEBDEVELOPMENT",
            "MOBILEAPP",
            "USERINTERFACE",
            "DATABASEMANAGEMENT",
            "BIGDATA",
            "DATAANALYTICS",
            "ARTIFICIALINTELLIGENCE",
            "IMAGEPROCESSING",
            "NATURALLANGUAGEPROCESSING",
            "COMPUTERVISION",
            "PYTHONISTHEBEST",
            "ILOVEPROGRAMMING",
            "HELLOGPT3",
            "CREATIVITY",
            "INNOVATION",
            "CODINGCHALLENGE",
            "EDUCATIONAL",
            "KNOWLEDGE",
            "TECHNOLOGY"
        ]

        # Initialiser les variables
        self.mot_a_deviner = tk.StringVar()
        self.nouveau_mot()

        self.lettres_devinees = set()
        self.lettres_incorrectes = set()
        self.tentatives_restantes = 10  # 10 tentatives au total

        # Créer l'interface
        self.creer_interface()

    def nouveau_mot(self):
        self.mot_a_deviner.set(random.choice(self.liste_de_mots))

    def creer_interface(self):
        self.label_titre = tk.Label(self.root, text="Jeu du Pendu", font=("Helvetica", 20, "bold"))
        self.label_titre.pack(pady=10)

        self.canvas_pendu = tk.Canvas(self.root, width=300, height=400)
        self.canvas_pendu.pack()

        self.label_mot = tk.Label(self.root, text=self.get_mot_affiche(), font=("Helvetica", 24))
        self.label_mot.pack(pady=20)

        self.label_lettres_incorrectes = tk.Label(self.root, text="Lettres incorrectes: ", font=("Helvetica", 12))
        self.label_lettres_incorrectes.pack()

        self.label_tentatives = tk.Label(self.root, text=f"Tentatives restantes : {self.tentatives_restantes}", font=("Helvetica", 14))
        self.label_tentatives.pack()

        self.entry_lettre = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry_lettre.pack(pady=10)

        self.bouton_recommencer = tk.Button(self.root, text="Recommencer", command=self.recommencer_jeu, font=("Helvetica", 14, "bold"))
        self.bouton_recommencer.pack()
        self.bouton_recommencer.pack_forget()

        # Lier la touche "Entrée" à la fonction proposer_lettre
        self.root.bind("<Return>", lambda event: self.proposer_lettre())

        self.actualiser_pendu()

    def get_mot_affiche(self):
        mot_affiche = ""
        for lettre in self.mot_a_deviner.get():
            if lettre in self.lettres_devinees:
                mot_affiche += lettre + " "
            else:
                mot_affiche += "_ "
        return mot_affiche.strip()

    def dessiner_pendu(self, x, y, tentatives_restantes):
        if tentatives_restantes < 10:
            # Barre verticale
            self.canvas_pendu.create_line(x, y, x, y + 180)

        if tentatives_restantes < 9:
            # Barre diagonale retournée (entre la barre verticale et la barre horizontale)
            self.canvas_pendu.create_line(x, y + 40, x + 40, y)

        if tentatives_restantes < 8:
            # Barre horizontale prolongée
            self.canvas_pendu.create_line(x, y, x + 60, y)

        if tentatives_restantes < 7:
            # Barre verticale
            self.canvas_pendu.create_line(x + 60, y, x + 60, y + 60)

        if tentatives_restantes < 6:
            # Rond
            self.canvas_pendu.create_oval(x + 40, y + 60, x + 80, y + 100)

        if tentatives_restantes < 5:
            # Barre verticale un peu longue
            self.canvas_pendu.create_line(x + 60, y + 100, x + 60, y + 150)

        if tentatives_restantes < 4:
            # Barre diagonale vers la gauche au milieu de la dernière barre verticale (sur la gauche)
            self.canvas_pendu.create_line(x + 60, y + 120, x + 40, y + 140)

        if tentatives_restantes < 3:
            # Barre diagonale vers la droite au milieu de la dernière barre verticale (sur la droite)
            self.canvas_pendu.create_line(x + 60, y + 120, x + 80, y + 140)

        if tentatives_restantes < 2:
            # Barre diagonale vers la gauche au bout de la dernière barre verticale (sur la gauche)
            self.canvas_pendu.create_line(x + 60, y + 150, x + 40, y + 180)

        if tentatives_restantes < 1:
            # Barre diagonale vers la droite au bout de la dernière barre verticale (sur la droite)
            self.canvas_pendu.create_line(x + 60, y + 150, x + 80, y + 180)

    def actualiser_pendu(self):
        self.canvas_pendu.delete("all")
        self.dessiner_pendu(150, 50, self.tentatives_restantes)

    def proposer_lettre(self):
        lettre_proposee = self.entry_lettre.get().upper()

        if lettre_proposee.isalpha() and len(lettre_proposee) == 1:
            if lettre_proposee not in self.lettres_devinees and lettre_proposee not in self.lettres_incorrectes:
                self.lettres_devinees.add(lettre_proposee)

                if lettre_proposee not in self.mot_a_deviner.get():
                    self.tentatives_restantes -= 1
                    self.lettres_incorrectes.add(lettre_proposee)

                self.actualiser_interface()

                if "_" not in self.get_mot_affiche():
                    self.fin_partie("Bravo, vous avez gagné!")
            else:
                self.message("Lettre déjà proposée!")
        else:
            self.message("Veuillez entrer une lettre valide!")

        self.entry_lettre.delete(0, tk.END)

        if self.tentatives_restantes == 0:
            self.fin_partie("Désolé, vous avez perdu. Le mot était: " + self.mot_a_deviner.get())

    def actualiser_interface(self):
        self.label_mot.config(text=self.get_mot_affiche())
        self.label_tentatives.config(text=f"Tentatives restantes : {self.tentatives_restantes}")
        self.label_lettres_incorrectes.config(text="Lettres incorrectes: " + ", ".join(sorted(self.lettres_incorrectes)))
        self.actualiser_pendu()

    def fin_partie(self, message):
        self.entry_lettre.config(state=tk.DISABLED)
        self.bouton_recommencer.pack(pady=10)
        self.message(message)

    def message(self, msg):
        messagebox.showinfo("Message", msg)

    def recommencer_jeu(self):
        self.entry_lettre.config(state=tk.NORMAL)
        self.bouton_recommencer.pack_forget()
        self.nouveau_mot()
        self.lettres_devinees.clear()
        self.lettres_incorrectes.clear()
        self.tentatives_restantes = 10
        self.actualiser_interface()

if __name__ == "__main__":
    root = tk.Tk()
    jeu = JeuDuPendu(root)
    root.mainloop()

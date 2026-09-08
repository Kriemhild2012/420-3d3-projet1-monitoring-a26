import tkinter as tk
from observers.observer import Observateur

class AffichageDISK(Observateur):

    def __init__(self, main_window: tk.Frame):
        # À compléter: Créez un LabelFrame "RAM", un Label pour le pourcentage et un Canvas pour la barre de progression
        self.frame_disque = tk.LabelFrame(main_window, text="Disque", padx=10, pady=10)
        self.frame_disque.pack(fill=tk.X, padx=10, pady=5)
        self.label_disque = tk.Label(self.frame_disque, text="0%", font=("Arial", 24, "bold"))
        self.label_disque.pack()
        self.canvas_disque = tk.Canvas(self.frame_disque, width=300, height=20, bg="white")
        self.canvas_disque.pack()

    def actualiser(self, sujet) -> None:
        # À compléter: Récupérez la valeur RAM depuis sujet.get_donnees()
        disk_value = sujet.get_donnees().get("disk")
        # À compléter: Mettez à jour le label et la barre
        self.label_disque.config(text=f"{disk_value:.1f}%")
        
        self._dessiner_barre(disk_value)

    def _dessiner_barre(self, valeur: float) -> None:
        # À compléter: 
        # Effacez le canvas
        # Calculez la largeur (300 * valeur / 100)
        # Choisissez la couleur : vert < 50%, orange < 80%, rouge sinon
        # Dessinez le rectangle
        self.canvas_disque.delete("all")
        largeur_disque = int(300 * valeur / 100)
        if valeur < 50:
            couleur_disque = "green"
        elif valeur < 80:
            couleur_disque = "orange"
        else:
            couleur_disque = "red"
        self.canvas_disque.create_rectangle(0, 0, largeur_disque, 20, fill=couleur_disque, outline="")
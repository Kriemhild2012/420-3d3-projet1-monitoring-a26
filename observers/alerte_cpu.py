import tkinter as tk
from observers.observer import Observateur

class AlerteCPU(Observateur):

    def __init__(self, main_window: tk.Frame, seuil: float = 80.0):
        # À compléter: Créez un LabelFrame "Alerte CPU" et un Label pour l'alerte
        self.label_alerte_cpu = tk.Label(main_window, text="", font=("Arial", 12), fg="red")
        self.label_alerte_cpu.pack()
        self.seuil = seuil

    def actualiser(self, sujet) -> None:
        # À compléter: Récupérez la valeur CPU depuis sujet.get_donnees()
        cpu_value = sujet.get_donnees().get("cpu")
        # À compléter: Mettez à jour le label d'alerte si nécessaire
        if cpu_value >= self.seuil:
            self.label_alerte_cpu.config(text=f"CPU critique: {self.seuil}%")
        else:
            self.label_alerte_cpu.config(text="")
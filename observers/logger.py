import tkinter as tk
from datetime import datetime
from observers.observer import Observateur

class LoggerFichier(Observateur):
    def __init__(self,main_window: tk.Frame):
        # --- Bouton log ---
        self.log_active = True
        self.bouton_log = tk.Button(main_window, text="Désactiver le log", command=self.toggle_log)
        self.bouton_log.pack(pady=10)
    
    def actualiser(self, sujet) -> None:
        # À compléter: Récupérez la valeur CPU depuis sujet.get_donnees()
        sys_value = sujet.get_donnees()
        self._cpu = sys_value.get("cpu")
        self._ram = sys_value.get("ram")
        self._disque = sys_value.get("disk")
        self.ecrireLog()

    def ecrireLog(self) -> None:
        # Écrire dans le fichier log
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = (
            f"{horodatage} | "
            f"CPU: {self._cpu:.1f}% | "
            f"RAM: {self._ram:.1f}% | "
            f"Disque: {self._disque:.1f}%\n"
        )
        if self.log_active:
            with open("monitoring.log", 'a') as f:
                f.write(ligne)
                print(f"Écriture dans le fichier log: {ligne.strip()}")


    def toggle_log(self) -> None:
        self.log_active = not self.log_active
        if self.log_active:
            self.bouton_log.config(text="Désactiver le log")
        else:
            self.bouton_log.config(text="Activer le log")
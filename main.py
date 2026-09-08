'''
import tkinter as tk
from datetime import datetime
import psutil


class App:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Monitoring système")
        self.fenetre.resizable(False, False)
        
        self.fenetre_cpu = tk.Toplevel(self.fenetre)
        self.fenetre_cpu.title("Monitoring CPU")
        self.Label_cpu_grand = tk.Label(self.fenetre_cpu, text="0%", font=("Arial", 72, "bold"))
        self.Label_cpu_grand.pack(padx=20, pady=20)
        

        # --- CPU ---
        self.frame_cpu = tk.LabelFrame(self.fenetre, text="CPU", padx=10, pady=10)
        self.frame_cpu.pack(fill=tk.X, padx=10, pady=5)
        self.label_cpu = tk.Label(self.frame_cpu, text="0%", font=("Arial", 24, "bold"))
        self.label_cpu.pack()
        self.canvas_cpu = tk.Canvas(self.frame_cpu, width=300, height=20, bg="white")
        self.canvas_cpu.pack()
        self.label_80_cpu = tk.Label(self.frame_cpu, text = "Avertissement: le CPU dépasse 80% d'utilisation", fg="red", font=("Arial", 12))
        self.label_80_cpu.pack()

        # --- RAM ---
        self.frame_ram = tk.LabelFrame(self.fenetre, text="RAM", padx=10, pady=10)
        self.frame_ram.pack(fill=tk.X, padx=10, pady=5)
        self.label_ram = tk.Label(self.frame_ram, text="0%", font=("Arial", 24, "bold"))
        self.label_ram.pack()
        self.canvas_ram = tk.Canvas(self.frame_ram, width=300, height=20, bg="white")
        self.canvas_ram.pack()

        # --- Disque ---
        self.frame_disque = tk.LabelFrame(self.fenetre, text="Disque", padx=10, pady=10)
        self.frame_disque.pack(fill=tk.X, padx=10, pady=5)
        self.label_disque = tk.Label(self.frame_disque, text="0%", font=("Arial", 24, "bold"))
        self.label_disque.pack()
        self.canvas_disque = tk.Canvas(self.frame_disque, width=300, height=20, bg="white")
        self.canvas_disque.pack()
        
        # --- Bouton log ---
        self.log_active = True
        self.bouton_log = tk.Button(self.fenetre, text="Désactiver le log", command=self.toggle_log)
        self.bouton_log.pack(pady=10)

        self.rafraichir()
        self.fenetre.mainloop()
        
    def toggle_log(self):
        self.log_active = not self.log_active
        if self.log_active:
            self.bouton_log.config(text="Désactiver le log")
        else:
            self.bouton_log.config(text="Activer le log")

    def rafraichir(self):
        # Lire les métriques
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        disque = psutil.disk_usage('/').percent

        # Mettre à jour CPU
        self.label_cpu.config(text=f"{cpu:.1f}%")
        self.canvas_cpu.delete("all")
        largeur_cpu = int(300 * cpu / 100)
        if cpu < 50:
            couleur_cpu = "green"
        elif cpu < 80:
            couleur_cpu = "orange"
        else:
            couleur_cpu = "red"
            
        if cpu >= 80:
            self.label_80_cpu.config(text = "Avertissement: le CPU dépasse 80% d'utilisation", fg="red", font=("Arial", 12))
        else:
            self.label_80_cpu.config(text="")
        self.canvas_cpu.create_rectangle(0, 0, largeur_cpu, 20, fill=couleur_cpu, outline="")
        
        self.Label_cpu_grand.config(text=f"{cpu:.1f}%")

        # Mettre à jour RAM
        self.label_ram.config(text=f"{ram:.1f}%")
        self.canvas_ram.delete("all")
        largeur_ram = int(300 * ram / 100)
        if ram < 50:
            couleur_ram = "green"
        elif ram < 80:
            couleur_ram = "orange"
        else:
            couleur_ram = "red"
        self.canvas_ram.create_rectangle(0, 0, largeur_ram, 20, fill=couleur_ram, outline="")

        # Mettre à jour Disque
        self.label_disque.config(text=f"{disque:.1f}%")
        self.canvas_disque.delete("all")
        largeur_disque = int(300 * disque / 100)
        if disque < 50:
            couleur_disque = "green"
        elif disque < 80:
            couleur_disque = "orange"
        else:
            couleur_disque = "red"
        self.canvas_disque.create_rectangle(0, 0, largeur_disque, 20, fill=couleur_disque, outline="")

        # Écrire dans le fichier log
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = (
            f"{horodatage} | "
            f"CPU: {cpu:.1f}% | "
            f"RAM: {ram:.1f}% | "
            f"Disque: {disque:.1f}%\n"
        )
        if self.log_active:
            with open("monitoring.log", 'a') as f:
                f.write(ligne)
                print(f"Écriture dans le fichier log: {ligne.strip()}")

        self.fenetre.after(2000, self.rafraichir)


if __name__ == "__main__":
    app = App()
'''

from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.disk_display import AffichageDISK
from observers.ram_display import AffichageRAM
from observers.logger import LoggerFichier
import tkinter as tk

#Initialisation du sujet et des observateurs
metriques = MetriquesSysteme()
root = tk.Tk()
cpu = AffichageCPU(root)
ram = AffichageRAM(root)
disk = AffichageDISK(root)
logger = LoggerFichier(root)

#Abonnement des observateurs au sujet
metriques.abonner(cpu)
metriques.abonner(ram)
metriques.abonner(disk)
metriques.abonner(logger)

def rafraichir():
    metriques.actualiser_metriques()
    root.after(2000, rafraichir)

rafraichir()
root.mainloop()
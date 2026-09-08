from datetime import datetime
from observers.observer import Observateur

class LoggerFichier(Observateur):
    def __init__(self,nom_fichier: str = "monitoring.log"):
        self._nom_fichier = nom_fichier
    
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
        with open(self._nom_fichier, 'a') as f:
            f.write(ligne)
            print(f"Écriture dans le fichier log: {ligne.strip()}")
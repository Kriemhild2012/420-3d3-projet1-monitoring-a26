import tkinter as tk
from models.metrics import MetriquesSysteme
from observers.alerte_cpu import AlerteCPU
from observers.cpu_display import AffichageCPU
from observers.ram_display import AffichageRAM
from observers.disk_display import AffichageDISK
from observers.logger import LoggerFichier
 
class Dashboard(tk.Tk):
 
    INTERVALLE_MS = 2000
 
    def __init__(self, metriques: MetriquesSysteme):
        super().__init__()
        self.title("Monitoring système")
        self._metriques = metriques
                # --- Bouton log ---
        self.bouton_log = tk.Button(self, text="Désactiver le log", command=self.toggle_log)
        self.bouton_log.pack(pady=10)
 
        # 1. Créez les observateurs (AffichageCPU, AffichageRAM,
        #    AffichageDISK, LoggerFichier)
        self._creer_observateurs()
        # 2. Abonnez-les tous au sujet
        self._abonner_observateurs()
        # 3. Démarrez le rafraîchissement
        self._rafraichir()
 
    def _creer_observateurs(self) -> None:
        self._cpu = AffichageCPU(self)
        self._ram = AffichageRAM(self)
        self._disk = AffichageDISK(self)
        self._logger = LoggerFichier(self)
        self._cpu_alerte = AlerteCPU(self, seuil=80.0)
 
    def _abonner_observateurs(self) -> None:
        self._metriques.abonner(self._cpu)
        self._metriques.abonner(self._ram)
        self._metriques.abonner(self._disk)
        self._metriques.abonner(self._logger)
        self._metriques.abonner(self._cpu_alerte)
 
    def _rafraichir(self) -> None:
        # À compléter :
        # Appelez actualiser_metriques() sur les métriques
        self._metriques.actualiser_metriques()
        # Planifiez le prochain appel avec self.after()
        self.after(self.INTERVALLE_MS, self._rafraichir)
        
    def toggle_log(self) -> None:
        log_active = True
        if self._logger in self._metriques._observateurs:
            self._metriques.desabonner(self._logger)
            log_active = False 
        else:
            self._metriques.abonner(self._logger)
            log_active = True
        
        if log_active:
            self.bouton_log.config(text="Désactiver le log")
        else:
            self.bouton_log.config(text="Activer le log")
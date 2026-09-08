from models.metrics import MetriquesSysteme
from views.dashboard import Dashboard
 
metriques = MetriquesSysteme()
app = Dashboard(metriques)
app.mainloop()
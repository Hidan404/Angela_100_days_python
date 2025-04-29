from datetime import datetime



class SheetApi():
    def __init__(self,duracao,calorias):
        self.url = 'https://api.sheety.co/4a83785dd76a6d981cfc0442a524519d/planilhaDeCaminhada/workouts'
        self.novo_workout = {
            "workout": {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M"),
                "exercise": "Caminhada",
                "duration": duracao,
                "calories": calorias
            }
        }
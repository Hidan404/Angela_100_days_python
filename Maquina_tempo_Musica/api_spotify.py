import os

class DadosApi():
    def __init__(self):
        self.CLIENTE_ID = os.getenv("MTM_ID")
        self.CLIENTE_SECRET = os.getenv("MTM_SECRET")
        self.url = 'http://127.0.0.1:8888/callback'
        self.ESCOPO = "user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-private user-read-email streaming"

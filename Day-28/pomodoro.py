import flet as ft
import time
import threading
import pygame

class PomodoroApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_config()
        self.setup_ui()
        self.setup_events()

    def setup_config(self):
        """Configurações iniciais da aplicação"""
        self.page.title = "Pomodoro Pro"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_min_width = 800
        self.page.window_min_height = 600
        self.page.bgcolor = ft.Colors.BLUE_GREY_50
        
        # Configuração do Pygame Mixer
        pygame.mixer.init()

    def setup_ui(self):
        """Cria os elementos da interface"""
        # Elementos principais
        self.title = ft.Text(
            value="Pomodoro Pro",
            size=40,
            color=ft.Colors.DEEP_ORANGE_900,
            weight=ft.FontWeight.BOLD
        )

        self.timer_display = ft.Text(
            value="25:00",
            size=120,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD
        )

        # Botões
        self.btn_start = ft.ElevatedButton(
            text="Iniciar",
            width=200,
            height=50,
            bgcolor=ft.Colors.GREEN_800,
            color=ft.Colors.WHITE
        )

        self.btn_reset = ft.ElevatedButton(
            text="Resetar",
            width=200,
            height=50,
            bgcolor=ft.Colors.BLUE_800,
            color=ft.Colors.WHITE
        )

        # Layout principal
        self.page.add(
            ft.Column(
                [
                    ft.Container(self.title, margin=20),
                    ft.Container(
                        self.timer_display,
                        padding=30,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=20,
                        margin=20
                    ),
                    ft.Row(
                        [self.btn_start, self.btn_reset],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    def setup_events(self):
        """Configura os eventos dos botões"""
        self.btn_start.on_click = self.toggle_timer
        self.btn_reset.on_click = self.reset_timer

        # Estado inicial
        self.running = False
        self.mode = "work"  # work/break
        self.work_duration = 1500 # 25 minutos
        self.break_duration = 300   # 5 minutos
        self.remaining = self.work_duration
        self.thread = None

    def update_display(self):
        """Atualiza o display do timer"""
        mins, secs = divmod(self.remaining, 60)
        self.timer_display.value = f"{mins:02}:{secs:02}"
        self.page.update()

    def play_sound(self):
        """Toca o som de alarme"""
        try:
            pygame.mixer.music.load("Day-28/mixkit-classic-alarm-995.wav")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        except Exception as e:
            print(f"Erro de áudio: {e}")

    def toggle_timer(self, e):
        """Inicia/Pausa o timer"""
        self.running = not self.running
        self.btn_start.text = "Pausar" if self.running else "Iniciar"
        
        if self.running:
            self.thread = threading.Thread(target=self.run_timer, daemon=True)
            self.thread.start()
            
        self.page.update()

    def reset_timer(self, e):
        """Reinicia o timer para o estado inicial"""
        self.running = False
        self.mode = "work"
        self.remaining = self.work_duration
        self.btn_start.text = "Iniciar"
        self.update_display()

    def run_timer(self):
        """Executa a contagem regressiva"""
        while self.running and self.remaining > 0:
            time.sleep(1)
            self.remaining -= 1
            self.update_display()

        if self.remaining <= 0:
            self.play_sound()
            self.switch_mode()

    def switch_mode(self):
        """Alterna entre modo trabalho e pausa"""
        self.mode = "break" if self.mode == "work" else "work"
        self.remaining = self.break_duration if self.mode == "break" else self.work_duration
        self.running = False
        self.update_display()

def main(page: ft.Page):
    PomodoroApp(page)

if __name__ == "__main__":
    ft.app(target=main)
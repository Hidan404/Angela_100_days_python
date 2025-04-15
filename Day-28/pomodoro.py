import flet as ft
import time
import threading
import simpleaudio as sa

def main(page: ft.Page):
    page.title = "Pomodoro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
    #page.window_width = 400
    #page.window_height = 600
    page.window_fullscreen = True
    print(page.platform)
    segundos = 0
    execucao = False
    thread_timer = None


    subtitulo = ft.Text(
        value="Pomodoro",
        size=50,
        color=ft.colors.BLUE_900,
        text_align=ft.TextAlign.CENTER,  
        font_family="Arial"
    )
    page.add(subtitulo)

    # Timer label centralizado
    timer_label = ft.Text(
        value="00:00", 
        size=30,
        text_align=ft.TextAlign.CENTER  
    )
    def pausa_5_minutos():
        nonlocal execucao, segundos
        while execucao and segundos < 5:
            time.sleep(1)
            segundos += 1
            minutos = divmod(segundos, 60)
            timer_label.value = f"{minutos[0]:02d}:{minutos[1]:02d}"
            timer_label.update()

    def atualizar_relogio():
        nonlocal segundos, execucao
        while execucao and segundos < 15:
            time.sleep(1)
            segundos += 1
            minutos = divmod(segundos, 60)
            timer_label.value = f"{minutos[0]:02d}:{minutos[1]:02d}"
            timer_label.update()
        if segundos >= 15:
            musica = sa.WaveObject.from_wave_file("Day-28/mixkit-classic-alarm-995.wav")
            musica.play()
            musica.wait_done()
            timer_label.value = "Tempo esgotado!"
            timer_label.update()

    def timer_started(e):
        global execucao, segundos
        execucao = True
        segundos = 0
        timer_label.value = "00:00"
        timer_label.update()
        atualizar_relogio()

    def timer_started(e):
        nonlocal execucao, segundos, thread_timer
        if not execucao:
            execucao = True
            segundos = 0
            botao.text = "Parar"
            thread_timer = threading.Thread(target=atualizar_relogio)
            thread_timer.start()
        else:
            execucao = False
            botao.text = "Iniciar"
        
        page.update()    
      

       
    
    botao = ft.ElevatedButton(
        text="Iniciar",
        on_click=lambda e: timer_started(),
        width=200,
        height=50,
        bgcolor=ft.colors.BLUE_900
    )

    botao.on_click = timer_started

    
    page.add(
        ft.Column(
            [
                timer_label,
                ft.Container(botao, margin=ft.margin.only(top=20))  # Espaço entre os elementos
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza a coluna
            alignment=ft.MainAxisAlignment.CENTER  # Centraliza verticalmente
        )
    )

ft.app(target=main)
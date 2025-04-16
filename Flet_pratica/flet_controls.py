import flet as ft
import time



def main(page: ft.Page):
    texto = ft.Text("ola sabrina meu amor", color=ft.colors.RED_900)
    page.controls.append(texto)
    page.update()

    for i in range(10):
        t = ft.Text(f"Texto {i}", color=ft.colors.RED_900)
        page.add(t)
        #page.update()
        time.sleep(1)

    for i in range(10):
        page.controls.append(ft.Text(f"Linha: {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)    

        
    '''page.add(
    ft.Row(controls=[
        ft.Text(texto.value, color=ft.colors.RED_900),
        ft.Text("B"),
        ft.Text("C")
        ])
    )
    '''

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Nome", width=200),
            ft.ElevatedButton(text="Enviar", width=100)
        ])
    )
    


ft.app(target=main)    
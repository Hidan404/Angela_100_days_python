import flet as ft
import json

def main(page: ft.Page):
    page.title = "FlashCard"
   
    with open("flashcard capstone app project/palavras_1500.json", "r") as file:
        palavras = json.load(file)
        palavras_pt = [palavra["pt"] for palavra in palavras]
        palavras_en = [palavra["en"] for palavra in palavras]
   

    indice = 0
    mostrar_traducao = False

    texto_card = ft.Text(value=palavras_pt[indice], size=30, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, selectable=True)
    subtitulo = ft.Text("FlashCard", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE, selectable=True)
    subtitulo2 = ft.Text("Aprenda palavras em inglês", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE, selectable=True)
    
    def atualizar_card():
        if mostrar_traducao:
            texto_card.value = palavras_en[indice]
        else:
            texto_card.value = palavras_pt[indice]
        texto_card.update()

    def proximo_card(e):
        nonlocal indice
        indice = (indice + 1) % len(palavras_pt)
        atualizar_card()

    def mostrar_traducao_card(e):
        nonlocal mostrar_traducao
        mostrar_traducao = not mostrar_traducao
        atualizar_card()    


    containercard = ft.Container(
            content=texto_card,
            alignment=ft.alignment.center,
            padding=30,
            bgcolor=ft.colors.WHITE,
            border_radius=15,
            width=300,
            height=200,
            border=ft.border.all(1, ft.colors.GREY_300),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.GREY_400,
                offset=ft.Offset(2, 2),
                blur_style=ft.ShadowBlurStyle.NORMAL
            ),
            margin=ft.margin.only(top=120),
    )
    
      
    
    page.add(
        ft.Column(
            [    
                subtitulo,
                ft.Container(height=10),
                subtitulo2,
                ft.Container(height=10),
                containercard,
                ft.Row(
                    [
                        ft.IconButton(ft.icons.ARROW_BACK, on_click=proximo_card),
                        ft.IconButton(ft.icons.ARROW_FORWARD, on_click=proximo_card)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.IconButton(ft.icons.LANGUAGE, on_click=mostrar_traducao_card),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )



ft.app(target=main)
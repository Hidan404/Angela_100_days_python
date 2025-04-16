import flet as ft
import time


def main(page: ft.Page):
    page.title = "Todo List"

    def adicionar_tarefas(e):
        page.add(ft.Checkbox(label=campo_tarefa.value))
        campo_tarefa.value = ""
        campo_tarefa.focus()
        campo_tarefa.update()

    campo_tarefa = ft.TextField(hint_text="Digite uma tarefa", width=300)
    page.add(ft.Row([campo_tarefa, ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefas)]))

ft.app(target=main)        
import flet as ft


def main(page: ft.Page):
    page.title = "Conversor de milhas para km"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    def converter(e):
        try:
            milhas = float(miles_input.value)
            km = milhas * 1.60934
            result_label.value = f"{milhas} milhas é igual a {km:.2f} km"
        except ValueError:
            result_label.value = "Por favor, insira um número válido."
        result_label.update()

    miles_input = ft.TextField(label="Milhas", width=200)
    convert_button = ft.ElevatedButton(text="Converter", on_click=converter)
    result_label = ft.Text()

    page.add(miles_input, convert_button, result_label)
ft.app(target=main)
import flet as ft

def main(page: ft.Page):
    translations = {
        "English": "Most kids dream of scoring the perfect goal, I always dream of stopping it. - Iker Casillas",
        "Español": "La mayoría de los niños sueñan con marcar el gol perfecto, yo siempre sueño con detenerlo. - Iker Casillas",
        "cReol": "La plupart des enfants rêvent de marquer le but parfait, je rêve toujours de l'arrêter. - Iker Casillas"
    }

    quote_text = ft.Text(translations["English"], size=60)
    image = ft.Image(src="casillas.png", width=500)

    def update_quote(e):
        quote_text.value = translations[e.control.value]
        page.update()

    language_selector = ft.RadioGroup(
        on_change=update_quote,
        value="English",
        content=ft.Column([ft.Radio(value=lang, label=lang) for lang in translations])
    )

    page.add(image, quote_text, language_selector)

ft.app(target=main)

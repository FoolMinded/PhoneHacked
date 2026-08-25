from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class OpenIt(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="OpenIt",
            font_size="28sp"
        )

        question = Label(
            text="Are you an idiot?",
            font_size="22sp"
        )

        buttons = BoxLayout(
            orientation="horizontal",
            spacing=15,
            size_hint_y=None,
            height="60dp"
        )

        yes_button = Button(
            text="YES",
            font_size="20sp"
        )

        no_button = Button(
            text="NO",
            font_size="20sp"
        )

        buttons.add_widget(yes_button)
        buttons.add_widget(no_button)

        layout.add_widget(title)
        layout.add_widget(question)
        layout.add_widget(buttons)

        return layout


if __name__ == "__main__":
    OpenIt().run()

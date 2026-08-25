from kivy.app import App
from kivy.uix.label import Label


class OpenIt(App):

    def build(self):
        return Label(text="Phone Hacked")


if __name__ == "__main__":
    OpenIt().run()

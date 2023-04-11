from kivy.uix.widget import Widget
from kivy.app import App
import kivy
kivy.require('2.1.0')  # replace with your current kivy version !


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()

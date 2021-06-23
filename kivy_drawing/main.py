from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class MyApp(App):

    def build(self):
        w = Widget()
        with w.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=[100, 100], size=[100, 100])
        return w


if __name__ == '__main__':
    MyApp().run()

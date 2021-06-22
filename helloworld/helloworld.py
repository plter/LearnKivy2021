import os

os.environ['KIVY_IMAGE'] = "pil"

from kivy.app import App
from kivy.core.window import Window

Window.size = (400, 300)


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()

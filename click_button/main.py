from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        return Button(text="Click me", on_press=lambda e: print("Button clicked"))


if __name__ == '__main__':
    MyApp().run()

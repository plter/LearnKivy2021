from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (550, 400)


class MyApp(App):

    def build(self):
        return Builder.load_string("""
BoxLayout:
    orientation: "vertical"
    Button:
        text: "Button 1"
        on_press: app.btn_clicked()
    Button:
        text: "Button 2"
        """)

    def btn_clicked(self):
        print("Clicked")


if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.lang import Builder


class MyApp(App):

    def build(self):
        # return Builder.load_file("view.kv")
        return Builder.load_string("""
BoxLayout:
    Button:
        text: "Button 1"
    Button:
        text: "Button 2"
        """)


if __name__ == '__main__':
    MyApp().run()

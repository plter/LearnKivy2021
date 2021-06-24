import asyncio
import random

from kivy.app import App
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.widget import Widget


class Ball:

    def __init__(self, canvas) -> None:
        super().__init__()
        self._canvas = canvas
        self._x = 0
        self._y = 0
        self._speedX = random.random() * 3 + 1
        self._speedY = random.random() * 3 + 1

    def draw(self, max_size):
        self._canvas.add(Color(0, 0, 0, 1))
        self._canvas.add(Line(circle=(self._x, self._y, 20)))
        self._x += self._speedX
        self._y += self._speedY
        if (self._x < 0 and self._speedX < 0) or (self._x > max_size[0] and self._speedX > 0):
            self._speedX *= -1
        if (self._y < 0 and self._speedY < 0) or (self._y > max_size[1] and self._speedY > 0):
            self._speedY *= -1


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Balls"
        self._balls = []

    def build(self):
        w = Widget()
        for i in range(20):
            self._balls.append(Ball(w.canvas))
        return w

    async def draw_frames(self):
        while True:
            self.root.canvas.clear()
            self.root.canvas.add(Color(1, 1, 1, 1))
            self.root.canvas.add(Rectangle(pos=(0, 0), size=self.root.size))

            for b in self._balls:
                b.draw(self.root.size)
            await asyncio.sleep(0.02)
        pass

    def on_start(self):
        super().on_start()
        asyncio.get_event_loop().create_task(self.draw_frames())


if __name__ == '__main__':
    asyncio.run(MyApp().async_run())

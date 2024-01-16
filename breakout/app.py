import pyxel
from config import Config
from paddle import Paddle


class App:
    def __init__(self):
        pyxel.init(Config.WIDTH, Config.HEIGHT, title="Breakout")
        self._paddle = Paddle()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            return
        self._paddle.update()

    def draw(self):
        pyxel.cls(0)
        self._paddle.draw()


App()

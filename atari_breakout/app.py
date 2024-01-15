import pyxel
from config import Config


class App:
    def __init__(self):
        pyxel.init(Config.WIDTH, Config.HEIGHT, title="Atari Breakout")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)
        pyxel.circ(0, 0, 2, 8)


App()

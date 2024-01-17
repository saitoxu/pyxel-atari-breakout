import pyxel
from circle import Circle
from config import Config
from line import Line


class App:
    def __init__(self):
        pyxel.init(Config.WIDTH, Config.HEIGHT, title="Breakout")
        self._ball = Circle(Config.WIDTH / 2, Config.HEIGHT / 2, 4, color=14)
        self.lines = [
            Line(0, 0, 0, Config.HEIGHT),
            Line(0, 0, Config.WIDTH, 0),
            Line(Config.WIDTH, 0, Config.WIDTH, Config.HEIGHT),
            Line(0, Config.HEIGHT, Config.WIDTH, Config.HEIGHT),
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            return

        ball = self._ball
        ball._velocity = ball._velocity.mul(ball._deceleration)
        ball.move(ball._velocity.x, ball._velocity.y)

        for line in self.lines:
            ball.collided_with_line(line)

    def draw(self):
        pyxel.cls(0)
        self._ball.draw()


App()

import pyxel
from circle import Circle
from config import Config
from line import Line
from rectangle import Rectangle


class App:
    def __init__(self):
        pyxel.init(Config.WIDTH, Config.HEIGHT, title="Breakout", fps=30)
        self.ball = Circle(Config.WIDTH / 2, Config.HEIGHT / 2, 4, color=14)
        self.lines = [
            Line(0, 0, 0, Config.HEIGHT),
            Line(0, 0, Config.WIDTH, 0),
            Line(Config.WIDTH, 0, Config.WIDTH, Config.HEIGHT),
            Line(0, Config.HEIGHT, Config.WIDTH, Config.HEIGHT),
        ]
        _len = 80
        self.bricks = [
            Rectangle(8, 8, _len, _len, color=10),
            Rectangle(
                Config.WIDTH - _len - 8,
                8,
                _len,
                _len,
                color=9,
            ),
            Rectangle(
                8,
                Config.HEIGHT - _len - 8,
                _len,
                _len,
                color=8,
            ),
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            return

        ball = self.ball
        ball._velocity = ball._velocity.mul(ball._deceleration)
        ball.move(ball._velocity.x, ball._velocity.y)

        for line in self.lines:
            ball.collided_with_line(line)
        for brick in self.bricks:
            ball.collided_with_rect(brick)

    def draw(self):
        pyxel.cls(0)
        self.ball.draw()
        for brick in self.bricks:
            brick.draw()


App()

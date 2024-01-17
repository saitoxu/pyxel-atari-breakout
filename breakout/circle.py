import math
import random

import pyxel
from line import Line
from rectangle import Rectangle
from shape import Shape
from vector import Vector


class Circle:
    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        restitution: float = 1.0,
        deceleration: float = 1.0,
        color: int = 0,
    ) -> None:
        self._x = x
        self._y = y
        self._radius = radius
        self._restitution = restitution
        self._deceleration = deceleration
        self._shape = Shape.CIRCLE
        self._color = color
        self._velocity = Vector(
            random.randint(-20, 20), random.randint(-20, 20)
        )

    def move(self, dx: float, dy: float) -> None:
        self._x += dx
        self._y += dy

    def is_hit(self, x: float, y: float) -> bool:
        d2 = math.pow(x - self._x, 2) + math.pow(y - self._y, 2)
        return d2 <= math.pow(self._radius, 2)

    def collided_with_rect(self, r: Rectangle) -> None:
        nx = max(r._x, min(self._x, r._x + r._width))
        ny = max(r._y, min(self._y, r._y + r._height))

        if not self.is_hit(nx, ny):
            return

        d2 = math.pow(nx - self._x, 2) + math.pow(ny - self._y, 2)
        overlap = abs(self._radius - math.sqrt(d2))
        mx, my = 0, 0

        if ny == r._y:
            my = -overlap  # 上辺衝突
        elif ny == r._y + r._height:
            my = overlap  # 下辺衝突
        elif nx == r._x:
            mx = -overlap  # 左辺衝突
        elif nx == r._x + r._width:
            mx = overlap  # 右辺衝突
        else:
            mx = -self._velocity.x
            my = -self._velocity.y

        self.move(mx, my)
        if mx != 0:
            self._velocity = self._velocity.mul(-self._restitution, 1)
        if my != 0:
            self._velocity = self._velocity.mul(1, -self._restitution)

    def collided_with_line(self, line: Line) -> None:
        v0 = Vector(
            line._x0 - self._x + self._velocity.x,
            line._y0 - self._y + self._velocity.y,
        )
        v1 = self._velocity
        v2 = Vector(line._x1 - line._x0, line._y1 - line._y0)
        cv1v2 = v1.cross(v2)
        if cv1v2 == 0:
            return
        t1 = v0.cross(v1) / cv1v2
        t2 = v0.cross(v2) / cv1v2
        crossed = (0 <= t1 and t1 <= 1) and (0 <= t2 and t2 <= 1)

        if crossed:
            self.move(-self._velocity.x, -self._velocity.y)
            dot0 = self._velocity.dot(line._norm)
            vec0 = line._norm.mul(-2 * dot0)
            self._velocity = vec0.add(self._velocity)
            self._velocity = self._velocity.mul(
                line._restitution * self._restitution
            )

    def draw(self) -> None:
        pyxel.circ(self._x, self._y, self._radius, self._color)

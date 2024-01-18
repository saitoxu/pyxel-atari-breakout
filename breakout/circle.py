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
        self._velocity = Vector(-4, -4)

    def move(self, dx: float, dy: float) -> None:
        self._x += dx
        self._y += dy

    def collided_with_rect(self, r: Rectangle) -> bool:
        for line in r._lines:
            collided = self.collided_with_line(line)
            if collided:
                return True
        return False

    def collided_with_line(self, line: Line) -> bool:
        v0 = Vector(
            line._x0 - self._x + self._velocity.x,
            line._y0 - self._y + self._velocity.y,
        )
        v1 = self._velocity
        v2 = Vector(line._x1 - line._x0, line._y1 - line._y0)
        cv1v2 = v1.cross(v2)
        if cv1v2 == 0:
            return False
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
        return crossed

    def draw(self) -> None:
        pyxel.circ(self._x, self._y, self._radius, self._color)

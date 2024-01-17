import math

from shape import Shape
from vector import Vector


class Line:
    def __init__(
        self,
        x0: float,
        y0: float,
        x1: float,
        y1: float,
        restitution: float = 1.0,
    ) -> None:
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1
        self._restitution = restitution
        self._shape = Shape.LINE
        self._vec = Vector(x1 - x0, y1 - y0)
        length = math.sqrt(math.pow(self._vec.x, 2) + math.pow(self._vec.y, 2))
        self._norm = Vector(y0 - y1, x1 - x0).mul(1 / length)

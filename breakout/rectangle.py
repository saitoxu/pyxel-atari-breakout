import pyxel
from line import Line
from shape import Shape


class Rectangle:
    def __init__(
        self, x: float, y: float, width: float, height: float, color: int = 0
    ) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._shape = Shape.RECTANGLE
        self._lines = [
            Line(x, y, x + width, y),
            Line(x + width, y, x + width, y + height),
            Line(x + width, y + height, x, y + height),
            Line(x, y + height, x, y),
        ]
        self._deceleration = 0.0

    def draw(self) -> None:
        pyxel.rect(self._x, self._y, self._width, self._height, self._color)

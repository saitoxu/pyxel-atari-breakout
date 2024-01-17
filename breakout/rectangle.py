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
        self._deceleration = 0.0

    def is_hit(self, x: float, y: float) -> bool:
        return (
            self._x <= x
            and x <= self._x + self._width
            and self._y <= y
            and y <= self._y + self._height
        )

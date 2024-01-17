class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def add(self, vector: "Vector") -> "Vector":
        return Vector(self.x + vector.x, self.y + vector.y)

    def mul(self, x: float, y: float = None) -> "Vector":
        _y = y if y is not None else x
        return Vector(self.x * x, self.y * _y)

    def dot(self, vector: "Vector") -> float:
        return self.x * vector.x + self.y * vector.y

    def cross(self, vector: "Vector") -> float:
        return self.x * vector.y - self.y * vector.x

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

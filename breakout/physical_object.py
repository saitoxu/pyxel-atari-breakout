from object_type import ObjectType


class PhysicalObject:
    def object_type(self) -> ObjectType:
        raise NotImplementedError

    def collide_with(self, other_object: "PhysicalObject") -> None:
        raise NotImplementedError

    def update(self) -> None:
        raise NotImplementedError

    def draw(self) -> None:
        raise NotImplementedError

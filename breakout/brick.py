from object_type import ObjectType
from physical_object import PhysicalObject


class Brick(PhysicalObject):
    def object_type(self) -> ObjectType:
        return ObjectType.BRICK

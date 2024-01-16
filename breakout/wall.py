from object_type import ObjectType
from physical_object import PhysicalObject


class Wall(PhysicalObject):
    def object_type(self) -> ObjectType:
        return ObjectType.WALL

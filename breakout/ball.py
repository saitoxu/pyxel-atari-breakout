from object_type import ObjectType
from physical_object import PhysicalObject


class Ball(PhysicalObject):
    def object_type(self) -> ObjectType:
        return ObjectType.BALL

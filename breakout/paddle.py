from object_type import ObjectType
from physical_object import PhysicalObject


class Paddle(PhysicalObject):
    """
    板を表すクラス。
    """

    def __init__(self):
        """
        板の描画に必要な情報を管理するインスタンス変数を初期化する。
        """
        pass

    def object_type(self) -> ObjectType:
        return ObjectType.PADDLE

    def update(self) -> None:
        """
        ユーザーからの入力を受け取り、板の位置を更新する。
        """
        pass

    def draw(self) -> None:
        """
        板を描画する。
        """
        pass

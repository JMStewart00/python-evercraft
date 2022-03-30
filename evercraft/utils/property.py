# self is the instance of the descriptor you’re writing.
# obj is the instance of the object your descriptor is attached to.
# type is the type of the object the descriptor is attached to.
class EvercraftProperty():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

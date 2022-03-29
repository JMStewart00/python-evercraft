# this is where your character code will go
class Alignment():
    GOOD, NEUTRAL, EVIL = range(3)

class Character():
    DEFAULT_PROPS = {
        "_name": "Unnamed Hero",
        "_alignment": Alignment.NEUTRAL
    }

    def __init__(self, obj = None):
        if not isinstance(obj, dict) and obj is not None:
            raise ValueError("Sorry, you need to pass an object in to Character creation.")

        for key in self.DEFAULT_PROPS:
            if obj and key in obj.keys():
                value = obj[key]
            else:
                value = self.DEFAULT_PROPS[key]

            setattr(self, key, value)

    def __str__(self):
        return self._name

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def alignment(self):
        """The alignment property."""
        return self._alignment

    @alignment.setter
    def alignment(self, value):
        self._alignment = value


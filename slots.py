"""
slots (alohida mavzu) - memory managmentda ancha as qotadi va machina xotirasida kamroq joy egalay oladi.
"""


# Bad
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Good
class Point:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

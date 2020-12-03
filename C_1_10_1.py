class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def width(self):
        return self.x

    def height(self):
        return self.y

    def __str__(self):
        return f"Rectangle ({self.x}, {self.y}, {Rectangle.width(self)}, {Rectangle.height(self)})"

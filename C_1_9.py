
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Rectangle {self.a}*{self.b}"

    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Square {self.a}*{self.a}"

    def get_area(self):
        return self.a ** 2

class Circle:
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"Circle radius={self.a}"

    def get_area(self):
        return 3.14 * self.a**2
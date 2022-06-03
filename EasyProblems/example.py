class Rectangle(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __str__(self):
        return '(Rectangle: %s, %s)' % (self.width, self.height)


r1 = Rectangle(12, 24)
print(r1)

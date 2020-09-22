from lab_python_oop.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, leng, color):
        super().__init__(leng, leng, color)
        self.shape = 'Квадрат'

    def __repr__(self):
        return "{0} площадью {1} {2} цвета со стороной {3}".format(self.shape, self.area, self.color.color, self.weight)
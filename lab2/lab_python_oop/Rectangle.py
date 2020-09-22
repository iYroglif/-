from lab_python_oop.GeomFigure import GeomFigure
from lab_python_oop.FigureColor import FigureColor

class Rectangle(GeomFigure):
    def __init__(self, weight, height, color):
        self.shape = 'Прямоугольник'
        self.weight = weight
        self.height = height
        self.color = FigureColor(color)
        self.area = self.CalcArea()

    def CalcArea(self):
        return self.height * self.weight

    def __repr__(self):
        return "{0} площадью {1} {2} цвета шириной {3} и высотой {4}".format(self.shape, self.area, self.color.color, self.weight, self.height)
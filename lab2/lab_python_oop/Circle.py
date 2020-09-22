from lab_python_oop.GeomFigure import GeomFigure
from lab_python_oop.FigureColor import FigureColor
from math import pi

class Circle(GeomFigure):
    def __init__(self, radius, color):
        self.shape = 'Окружность'
        self.radius = radius
        self.color = FigureColor(color)
        self.area = self.CalcArea()

    def CalcArea(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return "{0} площадью {1:.2f} {2} цвета радиусом {3}".format(self.shape, self.area, self.color.color, self.radius)
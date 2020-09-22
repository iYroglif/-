from abc import ABC, abstractmethod

class GeomFigure(ABC):
    def __init__(self):
        self.shape
        self.__area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        if area < 0:
            raise Exception("Площадь не может быть меньше 0")
        else:
            self.__area = area

    @abstractmethod
    def CalcArea(self):
        pass

    def name(self):
        return self.shape
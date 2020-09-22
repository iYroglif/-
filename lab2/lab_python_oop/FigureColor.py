import pymorphy2

morph = pymorphy2.MorphAnalyzer()

class FigureColor:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        color = morph.parse(color)[0]
        self.__color = color.inflect({'gent'}).word
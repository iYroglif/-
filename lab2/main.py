from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

def main():
    r, c, s = Rectangle(21, 21, 'синий'), Circle(21, 'зеленый'), Square(21, 'красный')
    print(r, c, s, sep='\n')
    #print(s.name())

if __name__ == "__main__":
    main()
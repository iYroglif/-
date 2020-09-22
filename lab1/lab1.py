from sys import argv
from math import sqrt

def ReadCoefficient(coef):
    while True:
        try:
            return float(input("Введите коэффициент: {} = ".format(coef)))
        except ValueError:
            print("Проверьте правильность данных и попробуйте снова.")

print("Терентьев Владислав Олегович ИУ5-53")
print("Пример уравнения: a*x^4 + b*x^2 + c = 0, где a, b, c - коэффициенты.")
param = False
if len(argv) == 4:
    try:
        a = float(argv[1])
        b = float(argv[2])
        c = float(argv[3])
        param = True
        print("a = {0}, b = {1}, c = {2}".format(a, b, c))
    except ValueError:
        print("Проверьте правильность данных и попробуйте снова.")
while True:
    if param == False:
        a = ReadCoefficient("a")
        b = ReadCoefficient("b")
        c = ReadCoefficient("c")
    else:
        param = False
    d = b ** 2 - 4*a*c
    print("Дискриминант равен: ", d)
    print("Корни уравнения:")
    if a == 0:
        if b == 0:
            print("Вы ввели не уравнение.")
        elif c == 0:
            print("x = 0")
        elif -c/b > 0:
            print("x = {0}\nx = -{0}".format(sqrt(-c/b)))
        else:
            print("x = {0}\nx = -{0}".format(complex(0, sqrt(c/b))))
    elif d == 0:
        if b == 0:
            print("x = 0")
        elif -b / (2 * a) > 0:
            print("x = {0}\nx = -{0}".format(sqrt(-b / (2 * a))))
        else:
            print("x = {0}\nx = -{0}".format(complex(0, sqrt(b / (2 * a)))))
    elif d > 0:
        d = sqrt(d)
        if -b + d == 0:
            print("x = 0")
        elif (-b + d) / (2 * a) > 0:
            print("x = {0}\nx = -{0}".format(sqrt((-b + d) / (2 * a))))
        else:
            print("x = {0}\nx = -{0}".format(complex(0, sqrt(-(-b + d) / (2 * a)))))
        if -b - d == 0:
            print("x = 0")
        elif (-b - d) / (2 * a) > 0:
            print("x = {0}\nx = -{0}".format(sqrt((-b - d) / (2 * a))))
        else:
            print("x = {0}\nx = -{0}".format(complex(0, sqrt(-(-b - d) / (2 * a)))))
    else:
        print("x = {0}\nx = {1}".format(pow((-b + complex(0, sqrt(-d))) / (2 * a), 1/2), -pow((-b + complex(0, sqrt(-d))) / (2 * a), 1/2)))
        print("x = {0}\nx = {1}".format(pow((-b + complex(0, -sqrt(-d))) / (2 * a), 1/2), -pow((-b + complex(0, -sqrt(-d))) / (2 * a), 1/2)))
    if input("Выйти из программы? (Y - да, N - нет): ") == "Y":
        break
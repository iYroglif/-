# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.data = iter(items)
        self.uniq = set()
        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        if self.ignore_case:
            try:
                current = self.data.__next__().lower()
            except Exception:
                current = self.data.__next__()
        else:
            current = self.data.__next__()
        if current not in self.uniq:
            self.uniq.add(current)
            return current
        else:
            return self.__next__()

    def __iter__(self):
        return self

if __name__ == '__main__':
    from gen_random import gen_random

    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

    for i in Unique(data):
        print(i)

    data = gen_random(10, 1, 3)
    print('---')
    for i in Unique(data):
        print(i)

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('---')
    for i in Unique(data):
        print(i)

    print('---')
    for i in Unique(data, ignore_case=True):
        print(i)
from operator import itemgetter

class Detail:
    """Деталь"""

    def __init__(self, id, name, price, sup_id):
        self.id = id
        self.name = name
        self.price = price
        self.sup_id = sup_id

class Supplier:
    """Поставщик"""

    def __init__(self, id, name):
        self.id = id
        self.name = name

class DetSup:
    """'Детали поставщика' для реализации связи многие-ко-многим"""

    def __init__(self, sup_id, det_id):
        self.sup_id = sup_id
        self.det_id = det_id

# Поставщики
sups = [
    Supplier(1, 'GATES'),
    Supplier(2, 'NORMA'),
    Supplier(3, 'FINWHALE'),
    Supplier(4, 'CTR'),
]

# Детали
dets = [
    Detail(1, 'Ремень ГРМ', 362, 1),
    Detail(2, 'Хомут', 28, 2),
    Detail(3, 'Амортизатор двери', 622, 3),
    Detail(4, 'Тяга переднего стабилизатора', 600, 4),
    Detail(5, 'Колодки передние тормозные', 1193, 4),
]

dets_sups = [
    DetSup(1,1),
    DetSup(2,2),
    DetSup(3,3),
    DetSup(4,4),
    DetSup(4,5),

    DetSup(4,3)
]

def main():
    """Основная функция"""

    one_to_many = [(d.name, d.price, s.name) 
        for s in sups 
        for d in dets 
        if d.sup_id==s.id]
    
    many_to_many_temp = [(s.name, ds.sup_id, ds.det_id) 
        for s in sups 
        for ds in dets_sups 
        if s.id==ds.sup_id]
    
    many_to_many = [(d.name, d.price, dep_name) 
        for dep_name, sup_id, det_id in many_to_many_temp
        for d in dets if d.id==det_id]

    print('Задание В1')
    res_11 = list(filter(lambda x: x[0].startswith('А'), one_to_many))
    print(res_11)
    
    print('\nЗадание В2')
    res_12_unsorted = []
    for s in sups:
        s_dets = list(filter(lambda i: i[2]==s.name, one_to_many))    
        if len(s_dets) > 0:
            s_prices = [price for _,price,_ in s_dets]
            s_prices_min = min(s_prices)
            res_12_unsorted.append((s.name, s_prices_min))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print('\nЗадание В3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)

if __name__ == '__main__':
    main()
    
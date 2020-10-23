def print_result(func_to_decorate):

    def decorated_func(*args):
        print(func_to_decorate.__name__)
        rs = func_to_decorate(*args)
        if type(rs) == list:
            for item in rs:
                print(item)
        elif type(rs) == dict:
            for i, k in rs.items():
                print(i, '=', k)
        else:
            print(rs)
        return rs

    return decorated_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
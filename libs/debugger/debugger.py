import sys
from pprint import pp


def de(obj, prefix=''):
    pp(exit(obj))


def d(obj, prefix=''):
    pp(obj)


def arrd(arr: list, prefix='') -> list:
    my_type = '[' + arr.__class__.__name__ + '(' + str(len(arr)) + ')]:'
    print(prefix, my_type, sep='')
    prefix += '    '
    for i in arr:
        if type(i) in (list, tuple, dict, set):
            print(i, e)
        else:
            if isinstance(arr, dict):
                print(
                    prefix, i, ': (', arr[i].__class__.__name__, ') ', arr[i], sep='')
            else:
                print(prefix, '(', i.__class__.__name__, ') ', i, sep='')

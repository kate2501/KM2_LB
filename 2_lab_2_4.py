import sys 
from collections.abc import Iterable
import argparse

parser = argparse.ArgumentParser(description='Input from file')
parser.add_argument('Iterableobj', type=list, help='Open file')
args=parser.parse_args()


def flatten_it(obj):
    tmp = []
    while obj:
        s, k = obj[-1], obj[:-1]
        obj = list(k)
        if isinstance(s, Iterable):
            obj.extend(s)
        else:
            tmp.append(s)
    tmp.reverse()
    return tmp

ff = ((1,2),3,(([])))
b = [[1], 2, [[3, 4], 5], [[[]]], [[[6],5],1], 7, 8]
a = sys.argv[1]
print(type(a)) 
print(a)
c = flatten_it(b)
print(ff)
print(b)
print(c)


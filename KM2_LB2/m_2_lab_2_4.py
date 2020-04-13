import argparse


def flatten_it(obj): #non recursive(this function was used futher)
    if isinstance(obj, (list, tuple)):
        while obj:
            s, k = obj[0], obj[1:]
            if s == ... or s == obj:
                raise ValueError
            for el in k:
                if el == ... or el == obj:
                    raise ValueError
            obj = list(k)
            if isinstance(s, (list, tuple, set)):
                obj = list(s) + obj
            elif isinstance(s, dict):
                yield dict(flatten_dict(s))
            else:
                yield s
    else:
        yield obj

def flatten_it_rec(obj): #how to do this with recursion
    if isinstance(obj, (list, tuple)):
        for el in obj:
            if el == obj or el == ...:
                raise ValueError
            if not isinstance(el, (list, tuple)):
                yield el
            elif isinstance(s, dict):
                yield dict(flatten_dict(s))
            else:
                yield from flatten_it_rec(el)
    else:
        yield obj

def flatten_dict(d):
    for k, v in d.items():
        if type(v) is dict:
            for k1, v1 in flatten_dict(v):
                if isinstance(v1, (list, tuple, set)):
                    yield str(k) + '_' + str(k1), list(flatten_it(v1))
                else:
                    yield str(k) + '_' + str(k1), v1
        else:
            yield k, v

def flatten(obj):
    if isinstance(obj, dict):
        return flatten_dict(obj)
    else:
        return flatten_it(obj)

def main():
    parser = argparse.ArgumentParser(description="Input for flattening")
    parser.add_argument('arr', type=str, help="To be flattened")
    args = parser.parse_args()
    print("Before: ", eval(args.arr))
    print("After: ", list(flatten(eval(args.arr))))
    #ini_dict = [("h", "h"),{'f': {1: {'for': ([(1,7, {1,(2,3)}),1,[], 
    #        {'s': {'s1': {'s2': 3}}}, (9,0)])}}, 
    #        'for': {'3': {3: 3}}, 
    #        25: {'for': {'a': 1, 'for': 4}}}, [1,2, [5]]]
    #print(list(flatten(ini_dict)))

if __name__ == "__main__":
    main()

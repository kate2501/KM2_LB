__all__ = ['flatten']

def flatten_it(obj):
    if isinstance(obj, list):
        tmp = []
        while obj:
            s, k = obj[-1], obj[:-1]
            obj = list(k)
            if isinstance(s, (list, tuple, set)):
                obj.extend(s)
            elif isinstance(s, dict):
                tmp.append(flatten_dict(s))
            else:
                tmp.append(s)
        tmp.reverse()
        return tmp
    return obj

def flatten(obj):
    if isinstance(obj, dict):
        return flatten_dict(obj)
    return flatten_it(obj)

def flatten_dict(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (str(key) + '_' + str(k), v) 
                for k, v in flatten_dict(value).items() ]
        return [ (key, flatten_it(value)) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)

def main():
    ini_dict = [("h", "h"),{'f': {1: {'for': ([(1,7, {1,(2,3)}),1,[], 
            {'s': {'s1': {'s2': 3}}}, (9,0)])}}, 
            'for': {'3': {3: 3}}, 
            25: {'for': {'a': 1, 'for': 4}}}, [1,2, [5]]]
    print(flatten(ini_dict))

if __name__ == "__main__":
    main()
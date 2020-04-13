import math

def to_json(obj, file=' '):
    if file == ' ':
        if isinstance(obj, bool):
            return bool_to_string(obj)
        if obj is None:
            return none_to_string()
        if isinstance(obj, int):
            return int_to_string(obj)
        if isinstance(obj, float):
            return str(obj)
        if isinstance(obj, str):
            return str_to_string(obj)
        if isinstance(obj, (list, tuple)):
            return array_to_string(obj)
        if isinstance(obj, dict):
            return dict_to_string(obj)
        raise ValueError
    else:
        with open(file, "a") as f:
            f.write(to_json(obj, ' '))

def int_to_string(i):
    string = ''
    while True:
        i, rem = divmod(i, 10)
        string = chr(ord('0') + rem) + string
        if i == 0:
            break
    return string

def str_to_string(string):
	return '\"' + string + '\"'

def bool_to_string(bl):
    if "%s" %bl == 'True':
        return 'true'
    else:
        return 'false'

def none_to_string():
    return 'null'

def single_array_to_string(lst):
    string = ''
    for el in lst:
        string += to_json(el) + ', '
    return '[' + string[:-2]+ ']'

def check_if_lists(lst):
    if isinstance(lst, (list,tuple, dict)):
        for el in lst:
            if isinstance(el, (list,tuple, dict)):
                return True
    return False


def array_to_string(lst):
    string = ''
    if check_if_lists(lst):
        for el in lst:
            if check_if_lists(el):
                string += array_to_string(el) + ', '
            else:
                string += to_json(el) + ', '
        return '[' + string[:-2]+ ']'
    if isinstance(lst, (list,tuple)):
        return single_array_to_string(lst)
    return to_json(lst)
    
def dict_to_string(dic):
    string = ''
    for key, value in dic.items():
        if isinstance(key, (int, bool, str, float)) or (key is None):
            if isinstance(key, str):
                string += to_json(key) + ': '
            else:
                string += str_to_string(to_json(key)) + ': '
            string += to_json(value) + ', '
        else:
            raise ValueError
    return '{' + string[:-2]+ '}'

def main():
    to_json(([{'h':{1:2}}, (3.5, [4,5])], [1, {3:(3.9,4)}]), 'file.txt')

if __name__ == "__main__":
    main()


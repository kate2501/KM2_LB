def from_json(obj):    
    obj = obj.strip()
    if obj[0] == "[" and obj[-1] == "]":
        return json_to_lists(obj)
    if obj[0] == "{" and obj[-1] == "}":
        return json_to_dict(obj)
    if obj.isdigit() or (obj[0] == '-' and obj[1:].isdigit()):
        return json_to_int(obj)
    if obj == 'true':
        return True
    if obj == 'false':
        return False
    if obj == 'null':
        return
    return json_to_string(obj)
    raise ValueError
    
def json_to_int(i):
    if i.isdigit():
        num = 0
        for el in i:
            num *= 10
            num += (ord(el)-48) * 10
        return num//10
    if i[0] == '-' and i[1:].isdigit():
        return -json_to_int(i[1:])
    raise ValueError

def json_to_string(text):
    return text[1:-1:]
    
def spl(lst):
    l = check(lst)
    f1, f2 = l[0], l[1]
    first, l, r = l[2], l[3], l[4]
    temp = []
    while f1 != -1 or f2 != -1:
        count = 1
        i = 1
        if first != 1:
            temp.extend(json_to_list(lst[1:first]))
        while count != 0:
            if lst[first+ i] == l:
                count += 1
            elif lst[first +i] == r:
                count -= 1
            i += 1
        temp.append(lst[first: (first +i)])
        lst = lst[(first +i):]
        l = check(lst)
        f1, f2 = l[0], l[1]
        first, l, r = l[2], l[3], l[4]
    if len(lst[:-1]) != 0:
        temp.extend(json_to_list(lst[:-1]))
    return temp

def check(lst):
    f1 = lst.find('{', 1)
    f2 = lst.find('[', 1)
    if f2 == -1:
        first, r, l = f1, '}', '{'
    elif f1 == -1:
        first, r, l = f2, ']', '['
    elif f1 < f2:
        first, r, l = f1, '}', '{'
    else:
        first, r, l = f2, ']', '['
    return (f1, f2, first, l, r)

def json_to_lists(lst):
    if lst.count('[') == 1:
        return [from_json(i) for i in json_to_list(lst[1:-1])]
    lst = spl(lst)
    return [from_json(i) for i in lst]

def json_to_list(lst):
    new_list = lst.split(',')
    if new_list.count('') != 0:
        new_list.remove('')
    if new_list.count(' ') != 0:
        new_list.remove(' ')
    final_list = []
    for el in new_list:
        final_list.append(el)
    return final_list

def json_to_dict(dic):
    r = dic.find(':')
    t = from_json(dic[r+1:-1])
    fin_dict = {json_to_string(dic[1:r]): t}
    return fin_dict

def json_to_float(fl):
    num = 0
    if fl.count('.') == 1:
        p = fl.find('.')
        num += json_to_int(fl[:p])
        fr = fl[p+1:]
        num += (json_to_int(fr)/(len(fr)+1)*10)
    return num,json_to_int(fl[:p]), fr


print(from_json('[1,false, {"1":[null, [{"2":1},5]},1, [[2,3],true], 7]'))
print([json_to_float('3.888')])

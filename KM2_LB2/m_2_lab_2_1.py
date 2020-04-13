import math  
import argparse

__all__ = ['sqrt_decomp']

def own_input():
    while True:
        print("Enter your array please")
        try:
            arr = list(map(float, input().split()))
            break
        except TypeError:
            print("Incorrect input")
    return arr

def find_borders(arr, val):
    try:
        borders = list(map(int, val.split()))
        if len(borders)!=2:
            print("Only 2 borders!!!") 
        elif borders[0]>borders[1]:
            print("First left, then right") 
        elif borders[0]<0 or borders[1]<0:
            print("Your borders don't correspond")
        elif borders[0]>len(arr) or borders[1]>len(arr):
            print("Your borders don't correspond")
        else:
            return borders
    except ValueError:
        print("Incorrect input")
    return []

def sqrt_decomp(a, l, r):
    new_len = math.ceil(math.sqrt(len(a)))
    b = [0] * new_len
    for i in range(len(a)):
        b[i // new_len] += a[i]
    c_l, c_r  = l // new_len, r // new_len
    k = 0 
    if l == r:
        return a[l]
    if c_l == c_r:
        for el in range(l, r): 
            k += a[el]
    else:
        for el in range(c_l + 1, c_r):
            k += b[el]
        for el in range(l, (c_l + 1)*new_len): 
            k += a[el]
        for el in range(c_r * new_len, r + 1): 
            k += a[el]
    return k

def main():
    parser = argparse.ArgumentParser(description='Input from file')
    parser.add_argument('-f', type=str, help='Open file')
    args = parser.parse_args()
    if args.f:
        try:
            tmp = []
            with open(args.f, 'r') as file:
                for val in file.read().split():
                    try:
                        tmp.append((int(val)))
                    except:
                        continue
            arr = tmp
        except FileNotFoundError:
                print('File does not exist')
    else:
        arr = own_input()
    print("Input 'exit' for exit")
    while True:
        val = input("Enter your borders(left,right) please:")
        if val == 'exit':
            break
        if find_borders(arr, val):
            borders = find_borders(arr, val)
            print(sqrt_decomp(arr, borders[0], borders[1]))
        else:
            continue

if __name__ == "__main__":
    main()

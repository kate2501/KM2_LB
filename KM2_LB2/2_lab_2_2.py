import sys
import random
import string
import argparse


def drawProgressBar(percent, barLen = 20):
    sys.stdout.write("\r")
    progress = ""
    for i in range(barLen):
        if i < int(barLen * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
    sys.stdout.flush()
 
def write_words(length):
    alph = string.ascii_letters
    word = ""
    for el in range(length):
        word += random.choice(alph)
    return word
 
def generate(mb, filename, border_l, border_s):   
    size = int(mb*(1024**2)) 
    count = 0
    L_l, R_l = border_l[0], border_l[1]
    L_s, R_s = border_s[0], border_s[1]
    with open(filename,'w',encoding = 'utf-8') as f:
        while count < size:
            choice_w = random.randrange(L_l, R_l+1)
            for word in range(choice_w):
                choice_l = random.randrange(L_s, R_s+1)
                if count+choice_l > size:
                    f.write(write_words(size-count))
                    count = size
                    break  
                f.write(write_words(choice_l))
                count += choice_l
                if count < size:
                    f.write(' ')
                    count += 1
            if count < size:  
                count += 2
                f.write("\n")
            drawProgressBar(count / size)
            if count == size:
            	return
 

def main():
    parser = argparse.ArgumentParser(description='Input from cmd')
    parser.add_argument('-f',  
        help='File at the end')
    parser.add_argument('-mb',  
        help='Numb. mbs')
    parser.add_argument('-w', nargs=2, type=int,  
        help='Numb. words in line(2 arg.)')
    parser.add_argument('-l', nargs=2, type=int, 
        help='Numb.letters in word(2 arg.)')
    args = parser.parse_args()
    try:
        if args.f:
            file = args.f
        else: raise ValueError
        if args.mb:
            mbs = float(args.mb)
            if mbs <= 0:
                raise ValueError
        else:
            raise ValueError
        if args.l:
            small = tuple(args.l)
            if not(0<small[0]<small[1]):
                raise ValueError
        else:
            small = (3, 10)
        if args.w:
            large = tuple(args.w)
            if not(0<large[0]<large[1]):
                raise ValueError
        else:
            large = (10, 100)
        generate(mbs,file + '.txt',large, small)
    except ValueError:
        print("Wrong input!")
 
if __name__ == "__main__":
    main()

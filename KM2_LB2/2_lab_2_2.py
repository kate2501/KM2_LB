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
    word = ""
    for el in range(length):
        word += random.choice(alph)
    return word
 
def generate(mb, filename, border_l = (10, 100), border_s = (3, 10)):   
    size = int(mb*(1024**2)) 
    count = 0
    L_l, R_l = border_l[0], border_l[1]
    L_s, R_s = border_s[0], border_s[1]
    with open(filename,'w',encoding = 'utf-8') as f:
        while count < size:
            choice_w = random.randrange(L_l, R_l)
            for word in range(choice_w):
                choice_l = random.randrange(L_s, R_s)
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
 
alph = string.ascii_letters
 
small = (3, 10)
large = (10, 100)
mb = 4
 
generate(mb,"file.txt")
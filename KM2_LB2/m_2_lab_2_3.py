import os
import uuid 
import argparse
import sys

def drawProgressBar(percent, barLen = 20):
    sys.stdout.write("\r")
    progress = ""
    for i in range(barLen):
        if i < int(barLen * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("[ %s ] %.0f%%" % (progress, percent * 100))
    sys.stdout.flush()

def update(pr):
    sys.stdout.write("\r")
    drawProgressBar(pr/192)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def split_file(filename):
    i, s =0, file_len(filename)
    f = open(filename)
    out = [open("outFile%d.txt" % k, "a") for k in range(64)]
    while True:
        buf = f.readline()
        if not buf:
            break
        k = i%64
        out[k].write(buf)
        i += 1
        update(i/s*64)
    f.close()
    for k in range(64):
        out[k].close
    return ["outFile%d.txt" % k for k in range(64)]

def merge(a,b):
    c = []
    a_ind, b_ind = 0, 0
    while a_ind<len(a) and b_ind<len(b):
        if a[a_ind] < b[b_ind]:
            c.append(a[a_ind])
            a_ind += 1
        else:
            c.append(b[b_ind])
            b_ind += 1
    if a_ind == len(a): 
        c.extend(b[b_ind:])
    else: 
        c.extend(a[a_ind:])
    return c

def merge_sort(a):
    mid = int(len(a)/2)
    if len(a) <= 1:
        return a
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    return merge(left, right)

def sort_file(filename, s):
    with open(filename, 'r') as file :
        filedata = file.readlines()
    with open(filename, "w") as f:
        for val in filedata:
            f.write(' '.join(merge_sort(val.strip().split())))
            f.write("\n")
    with open(filename, 'r') as file :
        filedata = file.readlines()
    with open(filename, "w") as f:
        f.write(''.join(merge_sort(filedata)))

def sort_files(out):
    for i in range(64):
        sort_file(out[i], i)
        update(i+64+i/64)

def merge_files(out):
    result = out[0]
    for i in range(1, 64):
        result = merge_2_files(result, out[i])
        update(i+128 + i/127)
    os.rename(result, "outfile.txt")


def merge_2_files(file1, file2):
    filename = str(uuid.uuid1())
    file_1, file_2 = open(file1, 'r'), open(file2, 'r')
    file_out = open(filename,'w')
    line_1, line_2 = file_1.readline(), file_2.readline()
    while line_1 and line_2:
        if line_1 < line_2:
            file_out.write(line_1)
            line_1 = file_1.readline()
        else:
            file_out.write(line_2)
            line_2 = file_2.readline()
    file_out.writelines([line_1, line_2])
    file_out.writelines(file_1.readlines())
    file_out.writelines(file_2.readlines())
    file_1.close()
    file_2.close()
    file_out.close()
    os.remove(file1)
    os.remove(file2)
    return filename
    
def main():
    parser = argparse.ArgumentParser(description='Inp.file name')
    parser.add_argument('-f',  
        help='Your file')
    args = parser.parse_args()
    try:
        if args.f:
            file = args.f
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("Your file wasn't found. Try again")
    out = split_file(file)
    sort_files(out)
    merge_files(out)


if __name__ == "__main__":
    main()



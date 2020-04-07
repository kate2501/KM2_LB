import os
import uuid 

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def split_file(filename):
    i = 0
    [open("outFile%d.txt" % i, "a") for i in range(16)]
    with open(filename) as f:
        while True:
            buf = f.readline()
            if not buf:
                break
            k = i%16
            out = open("outFile%d.txt" % k, "a")
            out.write(buf)
            out.close()
            i += 1
    return ["outFile%d.txt" % k for k in range(16)]

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

def sort_file(filename):
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
    for i in range(16):
        sort_file(out[i])

def merge_files(out):
    result = out[0]
    for i in range(1, 16):
        result = merge_2_files(result, out[i])
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
    out = split_file("file.txt")
    sort_files(out)
    merge_files(out)


if __name__ == "__main__":
    main()



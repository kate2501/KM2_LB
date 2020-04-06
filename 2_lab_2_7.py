import argparse

parser = argparse.ArgumentParser(description='leonardo number from cmd')
parser.add_argument('integer', type=int, default=-1, help='Your number from cmd')
args=parser.parse_args()

def leonardo(n):
    a = [1, 1]
    if n >= 1:
        #[a.append(a[i-1] + a[i-2] + 1) for i in range(2, n+1)]
        for i in range(2, n+1):
            a.append(a[i-1] + a[i-2] + 1)
    return a[-1]
def check_val(val):
    if isinstance(val,int):
        if val >= 0:
            return True
    else:
        return False

if args.integer:
    val = args.integer
    if check_val(val):
        print(leonardo(val))
else:
    print("Input 'exit' for exit")
    while True:
        val = input("Enter the number to find leonardo:")
        if val == 'exit':
            break
        if check_val(val):
            print(leonardo(val))
        else:
            continue


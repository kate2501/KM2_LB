import argparse

__all__ = ['leonardo']

def leonardo(n):
    a = [1, 1]
    if n >= 1:
        #[a.append(a[i-1] + a[i-2] + 1) for i in range(2, n+1)]
        for i in range(2, n+1):
            a.append(a[i-1] + a[i-2] + 1)
    return a[-1]

def check_val(val):
    try:
        val = int(val)
        if val >= 0:
            return True
        return False
    except ValueError:
        print('Wrong input!!!')


def main():
    parser = argparse.ArgumentParser(description='leonardo number from cmd')
    parser.add_argument('-i', type=int, help='Your number from cmd')
    args=parser.parse_args()
    if args.i:
        val = args.i
        if check_val(val):
            print(leonardo(val))
    else:
        print("'exit' for exit")
        while True:
            val = input("Enter the number to find leonardo:")
            if val == 'exit':
                break
            elif check_val(val):
                print(leonardo(int(val)))
            else:
                continue

if __name__ == "__main__":
    main()


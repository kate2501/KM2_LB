import argparse

__all__ = ['check_two']

def check_two(x):
	if str(bin(x)).count('1') == 1:
		return len(bin(x)[3:])
	return False

def check_val(val):
    try:
        val = int(val)
        return True
    except ValueError:
        return False
        print('Wrong input!!!')


def main():
	parser = argparse.ArgumentParser(description='your number from cmd')
	parser.add_argument('-i', type=int, help='Your number from cmd')
	args=parser.parse_args()
    if args.i:
        val = args.i
        if check_val(val):
            print(check_two(int(val)))
    else:
        print("'exit' for exit")
        while True:
            val = input("Enter your number:")
            if val == 'exit':
                break
            elif check_val(val):
                print(check_two(int(val)))
            else:
                continue

if __name__ == "__main__":
    main()


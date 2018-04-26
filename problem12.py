import sys


def problem1(input_str):
	# A
	print('A\'s answer:',input_str[::-1])
	
	# B
	reverse_str = [s[::-1] for s in input_str.split()]
	print('B\'s answer:', ' '.join(reverse_str))

def problem2(num):
	delete_num = num // 3 + num // 5 - (num // 15)*2

	print(num - delete_num)



if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print('usage: python3 problem12.py <problemId>')
		print('problemId: 1 or 2')
	# problem 1
	elif(sys.argv[1] == '1'):
		input_str = input('problem 1\'s input: ')
		problem1(input_str)

	# problem 2
	elif(sys.argv[1] == '2'):
		input_str = input('problem 2\'s input: ')
		problem2(int(input_str))
		


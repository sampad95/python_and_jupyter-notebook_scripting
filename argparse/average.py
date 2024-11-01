import argparse
parser = argparse.ArgumentParser(description ='sort some integers.')
parser.add_argument('numbers',
					metavar ='N',
					type = float,
					nargs ='+',
					help ='an integer for the accumulator')

parser.add_argument('sum',
					action ='store_const',
					const = sum)

parser.add_argument('len',
					action ='store_const',
					const = len)

args = parser.parse_args()
add = args.sum(args.numbers)
length = args.len(args.numbers)
average = add / length
print(average)


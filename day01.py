INPUT_FILE = 'input01.txt'

# sum the first and last digit in each line of text
def part_1(input):
	answer = 0
	for line in input:
		for char in line:
			if char.isdigit():
				first_digit = char
				break
		for char in reversed(line):
			if char.isdigit():
				second_digit = char
				break

		number = int(first_digit + second_digit)
		answer += number
	print(answer)

# sum the first and last number in each line of text (numbers spelled out with letters count too)
def part_2(input):
	answer = 0

	digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	written_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	reversed_digits = [digit[::-1] for digit in written_digits]

	all_digits = digits + written_digits
	all_digits_reversed = digits + reversed_digits

	# dicts to change written digits to the number
	word_2_number = {word: number for word, number in zip(written_digits, digits)}
	reversed_word_2_number = {word: number for word, number in zip(reversed_digits, digits)}

	for line in input:
		# find all the digits and their position in the line
		found_first_digits = {digit: line.find(digit) for digit in all_digits if line.find(digit) >= 0}
		# sort them in the order they first appear
		found_first_digits = {k: v for k, v in sorted(found_first_digits.items(), key=lambda item: item[1])}

		# grab the first digit, convert words to numbers if needed
		keys = list(found_first_digits.keys())
		first_digit = keys[0] if keys[0][0].isdigit() else word_2_number[keys[0]]

		# reverse the line, then find the first digit that appears (which is the last digit in the real line)
		found_second_digits = {digit: line[::-1].find(digit) for digit in all_digits_reversed if line[::-1].find(digit) >= 0}
		found_second_digits = {k: v for k, v in sorted(found_second_digits.items(), key=lambda item: item[1])}
		keys = list(found_second_digits.keys())
		second_digit = keys[0] if keys[0][0].isdigit() else reversed_word_2_number[keys[0]]

		number = int(first_digit + second_digit)
		print(number)
		answer += number
	print(answer)

if __name__ == '__main__':
	with open(INPUT_FILE) as f:
		input = [line.strip() for line in f.readlines()]
	part_1(input)
	part_2(input)
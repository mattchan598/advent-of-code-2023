import re

INPUT_FILE = 'input02.txt'

def part_1(input):
	RED = 12
	GREEN = 13
	BLUE = 14
	answer = 0

	for line in input:
		valid_game = True

		# find the game ID
		game_number, game = line.split(':')
		game_number = int(re.findall("\d+", game_number)[0])

		# get the sets of the game
		sets = game.split(';')
		
		for set in sets:
			# look for each color in each set
			check_red = re.findall("\d+ red", set)
			check_green = re.findall("\d+ green", set)
			check_blue = re.findall("\d+ blue", set)

			# check if the game is valid based on the number of each color
			if check_red:
				num_red = int(re.findall("\d+", check_red[0])[0])
				if num_red > RED:
					valid_game = False
					break
			if check_green:
				num_green = int(re.findall("\d+", check_green[0])[0])
				if num_green > GREEN:
					valid_game = False
					break
			if check_blue:
				num_blue = int(re.findall("\d+", check_blue[0])[0])
				if num_blue > BLUE:
					valid_game = False
					break
		
		answer += game_number if valid_game else 0
	print(answer)

if __name__ == '__main__':
	with open(INPUT_FILE) as f:
		input = [line.strip() for line in f.readlines()]
	part_1(input)
	# part_2(input)
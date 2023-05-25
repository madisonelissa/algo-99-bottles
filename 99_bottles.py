def bottle_song():
	inp = input('Enter number of bottles: ')
	bottles = int(inp)
	while bottles > 2:
		print(bottles, 'bottles of beer on the wall,', bottles, 'bottles of beer.\n Take one down and pass it around,', bottles-1, 'bottles of beer on the wall.')
		bottles = bottles - 1
	if bottles == 2:
		print(bottles, 'bottles of beer on the wall,', bottles, 'bottles of beer.\n Take one down and pass it around,', bottles-1, 'bottle of beer on the wall.')
		bottles = bottles - 1
	print('1 bottle of beer on the wall, 1 bottle of beer. \n Take one down and pass it around, no more bottles of beer on the wall.\n No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, 99 bottles of beer on the wall.')
bottle_song()git 
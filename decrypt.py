import math
import pyperclip

def main():
	myMessage = 'Cenoonommstmme oo snnio. s s c'
	myKey = 8
	plaitext = decryptMessage(myKey, myMessage)
	print(plaitext + '|')

def decryptMessage(key, message):
	numOfColumns = math.ceil(len(message)/key)
	#the number of rows our grid will need:
	numOfRows = key

	shaded_box = (numOfColumns * numOfRows) - len(message)

	plaintext = ['']*numOfColumns

	col = 0
	row = 0

	for symbol in message:
		plaintext[col] += symbol
		col += 1

		if(col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - shaded_box):
			col = 0
			row += 1

	return ''.join(plaintext)

if __name__ == '__main__':
	main()
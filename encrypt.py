import pyperclip


def main():
	myMessage = 'Common sense is not so common.'
	myKey  = 8

	ciphertext = encryptMessage(myKey ,myMessage)

	print(ciphertext + '|')

def encryptMessage(key, message):

	ciphertext = ['']*key # 8 strings will be generate according to the results.

	for col in range(key):
		pointer = col

		while pointer < len(message):

			ciphertext[col] += message[pointer]

			pointer += key

	return ''.join(ciphertext)

if __name__ == '__main__':
	main()
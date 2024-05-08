"""Bagels_mini , by shaddai465@gmail.com """

import random

NUM_DIGITS = 3
NUM_GUESSES = 10

def main():
	print('''Bagels, a deductive logic game. By Bishel.
			I am thinking of a {}-digit number with no repeated digits.
			Try to guess what it is.Here are some clues:
			Pico       One digit is correct in the wrong position.
			Fermi      One digit is correct in the right Position.
			Bagels     No digit is correct. 
		'''.format(NUM_DIGITS))

	while True: #Main game loop.
		SecretNum = getSecretNum() #This stores the secret number the player needs to guess:
		print('I have thought up a  number.')
		print('you have {} guesses to get it.'.format(MAX_GUESSES))

		numGuesses = 1
		while numGuesses <= Max_GUESSES:
			guess = ''
			#loop until a valid guess
			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print('Guess {#}: '.format(numGuesses))
				guess = input('> ')

			clues = getClues(guess,secretNum)
			print(clues)
			numGuesses += 1

			if guess == secretNum:
				break #they have guessed correctly,so breaking out  of this loop
			if  numGuesses > MAX_GUESSES:
				print('You ran out of guesses. ')
				print('The answer was {}.'. format(secretNum))

		#ask the player if they want to play again
		print('Do you want to play again? (yes or no)')
		if not input('> ').lower().startsWith('y'):
			break
		print('Thanks for playing!')



def getSecretNum():
	"""Returns a string made up of NUM_DIGITS unique random digits."""
	numbers = list('0123456789')
	random.shuffle(numbers) #Shuffle them into random order.

	#Get the first NUM_DIGITS digits in the list for the secret number:

	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum

def getClues(guess, secretNum):
	"""Returns a string with the Pico ,Fermi, Bagels clues for the guess and Secret number pair."""
	if guess == secertNum:
		return 'you got it'

	clues = []
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Fermi') #a correct Digit in a correct position
		elif guess[i] in secretNum: #a correct Digit in  wrong position
			clues.append('Pico') 
		if len(clues) == 0:
			return 'Bagels' #There is on correct digit in guess
		else :
			clues.sort()
			return ''.join(clues) #making a single list from a list of strings

# if the program is run instead of imported into other, run main

if  __name__ = '__main__':
	main()

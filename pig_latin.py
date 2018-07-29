

win = input('Enter a word:') # Asks user for input

def pig_latin(kigambo): # Define  function that takes one parameter

	if kigambo != str(kigambo):
		raise ValueError('Only words allowed.')
		
	kigambo = kigambo.lower() # This changes the string input to lowercase
	kigambo = list(kigambo) # This makes the input string a list
	i = 0

	for letter in kigambo: 
		nyukuta = kigambo[0]

		if i == 0:
			if (nyukuta == 'a' or nyukuta == 'e' or nyukuta == 'i' or nyukuta == 'o' or nyukuta == 'u'):
				kigambo.append('way')
				word = ''.join(kigambo)
				break
			else:
				kigambo.append(kigambo.pop(kigambo.index(letter)))
		else:
			if (nyukuta == 'a' or nyukuta == 'e' or nyukuta == 'i' or nyukuta == 'o' or nyukuta == 'u'):
				kigambo.append('ay')
				word = ''.join(kigambo)
				break
			else:
				kigambo.append(kigambo.pop(kigambo.index(letter)))

		i += 1

	return word

print(pig_latin(win))


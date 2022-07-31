cube = 8
epsilon = .001
increment = .01
guess = 0
while abs(guess**3 - cube) >= epsilon and guess < cube :
	guess += increment
if abs(guess**3 - cube) >= epsilon :
	print('Failed to find a close enough cube root of', cube, 'with these parameters')
else :
	print(guess, 'is close to the cube root of', cube)
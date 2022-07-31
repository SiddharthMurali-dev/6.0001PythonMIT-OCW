cube = 1000000
epsilon = .01
num_guesses = 1
if cube >= 1 :
	low = 0 
	high = cube
elif cube < -1 or cube > 0 :
	low = cube
	high = 1
else :
	low = -1
	high = cube
guess = (high + low) / 2
print('first guess =',guess)
while abs(guess**3 - cube) >= epsilon :
	if guess**3 < cube :
		low = guess
	else :
		high = guess
	guess = (high + low) / 2
	num_guesses += 1
	print(num_guesses, 'th guess = ', guess)
print('total number of guesses=',num_guesses)
print(guess, 'is close to the cube root of', cube)


cube = int(input('Give a number to find the cube root of: '))
#takes input
for guess in range(abs(cube) + 1) :
	print(guess)
	if guess**3 >= abs(cube) :
		break
if guess**3 != cube :
	print(cube, "is not a perfect cube")
else :
	if cube < 0 :
		guess = -guess
	print("The cube root of ", cube ,"is ", guess)


	xyz 
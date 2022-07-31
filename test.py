
# s = "demoi loops"
# # for index in range(len(s)):
# #     if s[index] == 'i' or s[index] == 'u':
# #         print("There is an i or u")

# for characttter in s:
#     if characttter == 'i' or characttter == 'u':
#         print("There is an i or u")
# cube = 729
# for guess in range(cube + 1) :
# 	print(guess)
# 	if guess**3 == cube :
# 		print("Cube root of", cube, "is", guess)
# print('done')
# for i in range(0,5) :
# 	print ('Haleluhah!')
# data supplied by the user
# base_annual_salary = float(input('Enter your annual salary: '))

# # data that is fixed
# portion_down_payment = 0.25
# rate_of_return = 0.04
# monthly_rate_of_return = rate_of_return / 12
# total_cost = 1000000
# down_payment = total_cost * portion_down_payment
# semi_annual_raise = 0.07
# months = 36

# # initially savings are zero. This variable is the core part of the decrementing
# # function used to stop the algorithm
# current_savings = 0.0

# # there is an acceptable margin of error for this algorithm
# epsilon = 100

# # define high and low bounds for the bisection search
# initial_high = 10000
# high = initial_high
# low = 0
# portion_saved = (high + low) // 2
# steps = 0

# # use bisection search to find the solution
# while abs(current_savings - down_payment) > epsilon:
#     steps += 1
#     current_savings = 0.0
#     annual_salary = base_annual_salary asdj
#     monthly_salary = annual_salary / 12
#     monthly_deposit = monthly_salary * (portion_saved / 10000)
#     for month in range(1, months + 1):
#         current_savings *= 1 + monthly_rate_of_return
#         current_savings += monthly_deposit
#         # problem states that semi-annual raises take effect the next month, so 
#         # mutate monthly_salary after mutating current_savings
#         if month % 6 == 0:
#             annual_salary *= 1 + semi_annual_raise
#             monthly_salary = annual_salary / 12
#             monthly_deposit = monthly_salary * (portion_saved / 10000)
#     prev_portion_saved = portion_saved
#     if current_savings > down_payment:
#         high = portion_saved
#     else:
#         low = portion_saved
#     # if the solution is outside of the search space on the high bound, low
#     # will eventually equal the inital high value. However, if we use integer
#     # division, low will be one less than high. As such, we round the average
#     # of high and low and cast to an int so that low and high will converge
#     # completely if the solution is outside of the search space on the high
#     # bound
#     portion_saved = int(round((high + low) / 2))
#     # if portion_saved is no longer changing, our search space is no longer
#     # changing (because the search value is outside the search space), so we
#     # break to stop an infinite loop
#     if prev_portion_saved == portion_saved:
#         break
    
# if prev_portion_saved == portion_saved and portion_saved == initial_high:
#     print('It is not possible to pay the down payment in three years.')
# else:
#     print('Best savings rate:', portion_saved / 10000)
#     print('Steps in bisection search:', steps) 
# def is_even(i) :
#     '''
#     Input: i, a positive integer
#     Returns : True, if i is even, otherwise False
#     '''
#     # print("inside is_even?") 
#     return i % 2 == 0

# check_if_even = float(input('Check if even. Enter number: '))
# print(is_even(check_if_even))

# def f(x) :
#     '''
#     Input: a value x
#     Returns : the value x + 1
#     '''
#     x = x + 1
#     print('in  f(x) : x =', x)
#     # return (x)

# # x = 3
# # z = f(x)
# # print(z)
# print(type(f)) 

# def f(y) :
#     return x

# x = 5 
# print(f(x))


# string = 'generic sentence'
# n = 0
# for i in string :
#     if i == 'e' :
#         n += 1
# print('There are', n,'e\'s')

# x = 3
# y = 4
# (x,y) = (y,x)
# a = (2, 'there')
# print(x)
# print(y)
# # print(string[n+2])
# import string
# print(type(string.ascii_lowercase))
# print(type(a))

# def mult(a,b) :
#     if b == 1 :
#         return a
#     else :
#         return a + mult(a,b-1)

# # print(mult(2,1))

# def factorial(n) :
#     if n == 1 :
#         return 1 
#     else :
#         return n * factorial(n-1)

# # print(factorial(52))
 
# def printMove(fr,to) :
#     print("move from " + str(fr) + " to " + str(to))

# def Towers(n, fr, to, spare) :
#     if n == 1 :
#         printMove(fr,to)
#     else :
#         Towers(n-1, fr, spare, to)
#         Towers(1, fr , to, spare)
#         Towers(n -1, spare, to , fr)

# Towers(3,'fr','to','spare')


# def isPalindrome(word) :
#     def toChars(word) :
#         word = word.lower()
#         word = word.replace(" ", "")
#         return word

#     def isPal(word) :
#         if len(word) <= 1 : #base case
#             return True
#         elif word[0] == word[-1] :
#             return isPal(word[1:-1])
#         else :
#             return False
#     return isPal(toChars(word))



# print(isPalindrome('Eve'))

# to count the number of prime numbers
# def isPrime(n) :
#     if n==0 or n==1 :
#         return False
#     else :
#         for i in range(2,int(n/2)+1) :
#             # print('i is' + str(i))
#             if n % i == 0 : 
#                 return False
#         return True    

# def countNoPrimes(i,j) :
#     count = 0
#     for n in range(i,j) :
#         if isPrime(n) == True :
#             print (n)
#             count = count + 1
#     print('The number of Prime numbers is ' + str(count))
#     return count

# countNoPrimes(-1,10)

# print('You are in the Lost Forest\n********\n********\n    :)    \n********\n********')
# inp = input('go left or right?').lower()
# count = 0
# if inp == 'left' :
#     print('You got out of the lost forest. GAME OVER')
#     # break
# while inp == 'right' :
#     count += 1
#     if count <= 3 :
#         print('You are in the Lost Forest\n********\n********\n    :)    \n********\n********')
#         inp = input('go left or right?').lower()
#     else :
#         print('You are in the Lost Forest\n********\n**   ***\n    (╯°□°)╯︵ ┻━┻     \n********\n********')
#         inp = input('go left or right?').lower()

# n = input("You are in the Lost Forest\n********\n********\n    :)    \n********\n********. Go left or right?").lower()
# while n != 'left' and n!= 'right' :
# 	n = input('INVALID INPUT. You are in the Lost Forest\n********\n********\n    :)    \n********\n********. Go left or right?').lower()
# count = 0
# while n == 'left' or n == 'right' :
# 	while n == 'right':
# 		count += 1
# 		if count < 3 :
# 			n = input("You are in the Lost Forest\n********\n********\n    :)    \n********\n********. Go left or right?").lower()
# 			while n != 'left' and n!= 'right' :
# 				n = input('INVALID INPUT. You are in the Lost Forest\n********\n********\n    :)    \n********\n********. Go left or right?').lower()
# 		else:
# 			n = input('You are in the Lost Forest\n********\n**   ***\n    (╯°□°)╯︵ ┻━┻     \n********\n********. Go left or right?').lower()
# 			while n != 'left' and n!= 'right' :
# 				n = input('INVALID INPUT. You are in the Lost Forest\n********\n********\n    :)    \n********\n********. Go left or right?').lower()
# 	if n == 'left' :
# 		print('You got out of the lost forest. \o/ GAME OVER')
# 		break




# import shutil

# # source_file = open('file.txt', 'r')
# # source_file.readline()
# # # this will truncate the file, so need to use a different file name:
# # target_file = open('file.txt.new', 'w')

# # shutil.copyfileobj(source_file, target_file)

# file_path = ""
# file_path = input("Input path of FASTA file of entire genome : ")

# ecoli_genome_file_source = open(file_path, 'r')
# ecoli_genome_file_source.readline()
# # print(ecoli_genome_file_source)
# ecoli_genome_file_new = open('ecoli_genome_file_source.new', 'w')
# shutil.copyfileobj(ecoli_genome_file_source, ecoli_genome_file_new)

# with open('ecoli_genome_file_source.new', 'r') as ecoli_genome_file :
# 	print(ecoli_genome_file.readline())

# import os
# path = input(r'Enter the path of the folder containing fasta files of genome sequences : ')
# entries = os.listdir(path)
# print(entries)
# # path = r"C:\Users\Siddharth Murali\Desktop\New folder\GCF_009832885.1_ASM983288v1_genomic.fna"
# file_path = f"{path}\\{entries[1]}"
# file = open(file_path)
# # print(file)

# columns = ['Strain', 'Genome Length', f'Number of matches of ']
# columns_string = ', '.join(columns)
# file_processed_data = open(r"D:\Productive\College\Internship\Output\output.txt", "w+")
# file_processed_data.write(columns_string)
# file_processed_data.write('\n')
# file_processed_data.write(columns_string)
# lines = file_processed_data.readlines()
# for line in lines :
# 	sline = line.split()

# def mult(a,b) :
# 	if b == 1 :
# 		return a
# 	else :
# 		return a + mult(a,b-1)

# def fact(n) :
# 	if n == 1:
# 		return n
# 	else :
# 		return n * fact(n-1)


# print(fact(20))

# def get_genome_name_one(n) :
# 	i = 0
# 	letter_index = 0
# 	for letter in n :
# 		# print(letter)
# 		if letter == '_' and i == 1:
# 			index = letter_index
# 			# print(index)
# 			return n[0 : index]
# 			break
# 		elif letter == '_' and i == 0:
# 			i += 1
# 			# print(f'i = {i}')
# 		letter_index += 1

# def get_genome_name_two(n) :
# 	i = 0
# 	letter_index = 0
# 	for letter in n :
# 		# print(letter)
# 		if letter == '_' and i == 3:
# 			# print('Oh thats one')
# 			first_index = letter_index
# 			# print(index)
# 			i += 1
# 		elif letter == '_' and i == 5:
# 			# print('Oh thats two')
# 			second_index = letter_index
# 			# print(index)
# 			return n[first_index+1:second_index]
# 			break
# 		elif letter == '_' and i >= 0:
# 			i += 1
# 			# print(f'i = {i}')
# 		letter_index += 1

# # print(get_genome_name_one('GCF_000007845.1_ASM784v1_vs_GCF_000008165.1_ASM816v1'))
# import os
# file_path = input('Enter file path : ')
# f = open(file_path)

# print(os.path.basename(file_path))
# lines = f.readlines()
# f.close()
# f_edited = open("D:\Productive\College\Internship\GCF_000007845.1_ASM784v1_vs_GCF_000008165.1_ASM816v1 - Copy_edited.fna", 'w')
# for x in lines :
# 	line_x = x.split('\t')
# 	line_x[0] = line_x[0] + 'ggwp'
# 	line_x_string = ' '.join(line_x)
# 	f_edited.write(line_x_string)
# print(lines_edited[0:2])
# line1 = lines[0].split('\t')
# print(line1)

# dic = {'ATA':1, 'ATC':3, 'TCC':1}
# print(dic)
# dic[]

# counts_patterns_dic = {}
# freq_patterns = []
# max_count = max(counts_patterns_dic.values())

# d = [0,1]
# d = [2]
# print(d)

# alphabet_list = string.ascii_lowercase()  
# print(alphabet_list)
# a = 2
# b= 3
# if a > 2:
# 	print('hi')
# elif b > 1:
# 	print('no')
# text = input('insert text')
# print(text[61:65])
# genome_file = open("D:\Productive\Courses\Bioinformatics Algorithms\/vibria_cholera_genome.txt", 'r')
# genome = genome_file.read()


import matplotlib
plt.plot([1,2,3,4])
plt.show() 

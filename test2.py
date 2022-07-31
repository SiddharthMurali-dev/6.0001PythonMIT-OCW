# an_letters = 'aefhilmnorsx'

# name =  input("I will cheer for you. What is your name? ")
# times = int(input("Emotional support needed (1-10): "))

# for char in name :
# 	if char.lower() in an_letters :
# 		print("Give me an " + char + '!')
# 	else : 
# 		print("Give me a " + char + '!')

# print("What does it spell?")
# print(name.upper() + '!'*times)

# total_cost = 1000000
# portion_down_payment = 0.25 #25%
# down_payment = total_cost * portion_down_payment
# semi_annual_raise = .07
# annual_return = 0.04

# starting_annual_salary = float(input('Enter your starting annual salary: '))

# one_hundred_dollars_as_epsilon = 100
# steps_in_bisection_search = 0
# possible_to_pay_in_three_years = True
# max_portion_saved_as_integer = 10000
# min_portion_saved_as_integer = 0
# best_portion_saved_as_integer = max_portion_saved_as_integer
# while True:
#     steps_in_bisection_search += 1
#     annual_salary = starting_annual_salary
#     best_portion_saved = best_portion_saved_as_integer / 10000
#     monthly_savings = (annual_salary / 12) * best_portion_saved
    
#     current_savings = 0.0
#     number_of_months = 0
#     while number_of_months <= 36:        
#         #print('current_savings: {}'.format(current_savings))
#         #print('number_of_months: {}'.format(number_of_months))
#         current_savings += monthly_savings + ((current_savings * annual_return) / 12)
#         number_of_months += 1
            
#         if number_of_months % 6 == 0:
#             annual_salary += annual_salary * semi_annual_raise
#             monthly_savings = (annual_salary / 12) * best_portion_saved            
    
#     #print('current_savings: {}'.format(current_savings))
#     if abs(current_savings - down_payment) <= one_hundred_dollars_as_epsilon:
#         break
    
#     if current_savings > down_payment:
#         max_portion_saved_as_integer = best_portion_saved_as_integer
#     else:
#         min_portion_saved_as_integer = best_portion_saved_as_integer
        
#     if min_portion_saved_as_integer >= max_portion_saved_as_integer:
#         possible_to_pay_in_three_years = False
#         break
        
#     best_portion_saved_as_integer = (max_portion_saved_as_integer + min_portion_saved_as_integer) // 2 # we will guess the value of this
    

# if possible_to_pay_in_three_years:
#     #print('current_savings: {}'.format(current_savings))
#     print('Best savings rate: {}'.format(best_portion_saved))
#     print('Steps in bisection search: {}'.format(steps_in_bisection_search))
# else:
#     print('It is not possible to pay the down payment in three years.')

# annual_salary = float(input("Enter your initial annual_salary: "))
# portion_saved = float(input("Enter percent of monthly you will save each month (in decimal): "))
# total_cost = 1000000
# semi_annual_raise = .07
# r = .04
# r_monthly = r/12
# portion_down_payment = .25
# current_savings = 0
# monthly_salary = annual_salary/12
# #how many months whill it take for a down payment?
# down_payment = portion_down_payment*total_cost
# no_months = 0
# six_month_counter = 0
# while current_savings <= down_payment :
# 	if six_month_counter == 6 :
# 		monthly_salary = monthly_salary + semi_annual_raise*monthly_salary
# 		six_month_counter = 0
# 	current_savings = current_savings + r_monthly*current_savings + portion_saved*monthly_salary
# 	no_months += 1
# 	six_month_counter += 1
# print(current_savings)
# print("It will take you " + str(no_months) + " months to make the down payment on your dream home")


a_list = [1, 2, 3, 4, 5]

for index, element in enumerate(a_list):
	if index % 2 == 0:
		print(element)
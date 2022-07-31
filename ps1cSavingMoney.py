#to find the best savings rate to pay down-payment in a given number of months

base_annual_salary = float(input('Enter initial salary: '))

#data that is fixed
semi_annual_raise = .07
monthly_rate_interest = .0033
total_cost = 1000000
down_payment = .25 * total_cost
No_months = 36

#degree of accuracy
epsilon = 100

low = 0
high = 10000
savings = (low + high) / 2

#initialising variables
total_savings = 0
No_steps = 0
while abs(total_savings - down_payment) >= epsilon :
	total_savings = 0
	No_steps += 1
	savings_rate = savings / 10000
	annual_salary = base_annual_salary
	for i in range(1, No_months + 1) :
		monthly_salary = annual_salary / 12
		monthly_savings = savings_rate * monthly_salary
		total_savings = total_savings + total_savings * monthly_rate_interest + monthly_savings
		if i % 6 == 0 :
			annual_salary = annual_salary + annual_salary * semi_annual_raise
	prev_savings = savings
	if total_savings < down_payment :
		low = savings
	else :
		high = savings
	savings = (high + low) / 2
	if savings == prev_savings :
		break
	# i = 0
if savings == prev_savings and savings == 10000 :
	print(No_steps)
	print("It is not possible to save", down_payment ,"with any savings rate in", No_months, "months with the base annual salary of", base_annual_salary)
else :
	print(No_steps, 'steps')
	print('best savings rate =', savings_rate)
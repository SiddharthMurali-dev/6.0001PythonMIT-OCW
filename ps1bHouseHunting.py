#with raises every six months
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter percentage of your salary to save, in decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('The semiannual salary raise : '))
portion_down_payment = .25 * total_cost
current_savings = 0
i = 0
n = 1
while current_savings < portion_down_payment :
	if n == 6 : #or if n % 6 == 0 (and remove the n = 0 )
		annual_salary = annual_salary + annual_salary * semi_annual_raise
		n = 0 #resets the counter
	monthly_salary = float(annual_salary/12)
	monthly_savings = (portion_saved * monthly_salary) 
	print(current_savings)
	current_savings = current_savings + (current_savings * .0033) + monthly_savings
	i += 1
	n += 1
else :
	print(i)
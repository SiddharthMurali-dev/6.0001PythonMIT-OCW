#without raise
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter percentage of your salary to save, in decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = .25 * total_cost
monthly_salary = float(annual_salary/12)
current_savings = 0
monthly_savings = (portion_saved * monthly_salary) 
i = 0
while current_savings < portion_down_payment :
	print(current_savings)
	current_savings = current_savings + (current_savings * .0033) + monthly_savings
	i = i + 1
else :
	print(i)
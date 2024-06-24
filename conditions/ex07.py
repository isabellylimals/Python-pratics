#aumento de salario
salary = float(input('Enter your salary: '))
if salary <= 1250.0:
    increase = (salary * 15) / 100
else:
    increase = (salary * 10) / 100
new_salary = salary + increase
print('Your salary of {}R$ has increased by {}R$ and is now {}R$.'.format(salary, increase, new_salary))

# WAP to calculate total salary of Employee based on Basic
# DA=10% Basic , TA=12% basic, HRA=15% basic

basic=float(input('Enter the total salary:'))
da= basic*10/100
ta= basic*12/100
hra= basic*15/100

total_salary= basic + da + ta + hra

print('DA=',da)
print('TA=',ta)
print('HRA=',hra)

print('Total_salary=',total_salary)

# Write a program to enter P,T,R and calculate compound intrest

### take input P,T,R
P =int(input('enter amount of the principal:'))
R =float(input('enter Rate of Intrest:'))
T =int(input('enter Time (Year):'))

###perform operation
CI =P*(1+R/100)**T-P

###Display Result
print(f'compound intrest is=',CI)
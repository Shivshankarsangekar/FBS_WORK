# Write a Program to find the Root of Quadratic Equation 

### Take input a,b,and c
import cmath
a =int(input('Enter a:'))
b =int(input('Enter b:'))
c =int(input('Enter c:'))

### perform operation
d =(b**2)-(4*a*c)
root1 =(b+cmath .sqrt(d))/(2*a)
root2 =(b-cmath .sqrt(d)/(2*a))


### Display Result 
print('Root 1=',root1)
print('Root 2=',root2)

# Write a program to enter P,T,R and calculate the simplest intrest 

### take input p,r,t
p = int(input('Enter the amount of principle:'))
r = float(input('Enter the Rate of intrest:'))
t = int(input('Enter the Time(Year):'))

#perform operation 
si = (p*r*t)/100

#Display Result 
print(f'simple intrest id {si}.')

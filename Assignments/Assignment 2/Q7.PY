# Take input a,b& c

num=int(input('Enter the three digit no:'))

a= num//100
b=(num//10)%10
c= num%10

sum=a+b+c

print('sum of digits=',sum)
# Write a program to input two angle from user and find third angle of the Triangle 

### Take input angle1 and angle2
angle1 = int(input('Enter the first Angle:'))
angle2 = int(input('Enter the second Angle:'))

###operation perform

angle3 = 180-(angle1+angle2)

###Display Result 
print('Third angle =',angle3)
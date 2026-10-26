# Find the Area and Circumference of Circle 

### Take input
import math
radius = float(input('Enter the radius:'))

### perform operation
Area = math.pi*radius**2
circumference = 2*math.pi*radius

### Display Result 
print('Area of Circle=',Area)
print('Circumference of Circle=',circumference)

# Convert the time entered in hh,min and sec into seconds.

#Take input
hh=int(input('Enter the Hours'))
mm=int(input('Enter the minutes'))
ss =int(input('Enter the seconds'))

#Perform Operation
total_seconds= (hh*60*60)+(mm*60)+ss

#Display Result
print('Total seconds=',total_seconds) 
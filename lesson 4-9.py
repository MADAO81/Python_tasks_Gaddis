#This program converts speeds from 60
#up to 130 km/h (in increments of 10 km) to mph

start_speed = 60 #Start speed
end_speed = 131 #End speed
increment = 10 #Increment
conversion_factor = 0.6214 #conversion factor

#Print the table headers
print("KPH\tMPH")
print("============")

#Print the speeds
for kph in range(start_speed, end_speed, increment):
    mph = kph * conversion_factor
    print(kph, '\t', format(mph,".2f"))
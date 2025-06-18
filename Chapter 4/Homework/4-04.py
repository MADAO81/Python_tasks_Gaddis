#distance traveled
vehicle_speed = int(input("Enter the speed of your vehicle, km/h:  "))
travel_time = int(input("Enter the time you traveled, hours: "))
distance_traveled = vehicle_speed * travel_time
print("Hour\tDistance traveled")
print("==========================")
for i in range(1,travel_time + 1):
    print(i,i * vehicle_speed,sep = "\t")
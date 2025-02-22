# Height of fall.
# When a body falls under the force of gravity, the following formula is used
# to determine the distance the body will travel in a certain time:
# d= 1/2gt2,
# where 'd' is the distance, m; 'g' = 9.8, m/s2; 't' is the time of the body’s fall,
# Write a function falling distance that takes the time of the body's fall (in seconds) as an argument.
# The function should return the distance in meters that the body has flown during this time interval.
# Write a program that calls this function in a loop, passes values from 1 to 10 as arguments,
# and displays the return value.
import math

G = 9.8  # acceleration of gravity


def main():
    time = 1
    for sec in range(1, 11):
        print(f" Time: {time} sec. Distance: {falling_distance(time):.2f} meters")
        time += 1


def falling_distance(time):
    distance = 0.5 * G * math.pow(time, 2)
    return distance


main()

# Kinetic energy.
# It is known from physics that a moving body has kinetic energy.
# The formula below can be used to determine the kinetic energy of a moving body:
# КЕ = 1/2mv2,
# where KE is kinetic energy; m is body mass, kg; v is body speed, m/s.
# Write a function called kinetic energy that takes as arguments the mass of an object
# (in kilograms) and its speed (in meters per second). This function should return the
# kinetic energy of the object. Write a program that asks the user to enter the mass and speed,
# and then calls the kinetic energy function to get the kinetic energy of the object.
import math
def main():
    mass_of_body = float(input("Enter the body mass, kilograms: "))
    speed = float(input("Enter the speed of the body, meters per second: "))
    print(f"Kinetic energy of this body will be: "
          f"{kinetic_energy(mass_of_body,speed):,.2f}, Joules")

def kinetic_energy(m,s):
    ke = 0.5 * m * math.pow(s,2)
    return ke

main()
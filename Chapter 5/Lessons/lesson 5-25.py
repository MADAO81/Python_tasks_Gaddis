# This program calculates the length of the hypotenuse of a right triangle
import math

def main():
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))
    
    c = math.hypot(a,b)
    
    print("Length of hypotenuse is: ", c)
    
main()
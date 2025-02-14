# This program allows the user to select various
# geometric calculations from the menu. 
# The program imports the 'circle' and 'rectangle' modules.
import circle
import rectangle

# Constants for menu items.
AREA_CIRCLE_CHOICE = 1 
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# Main function
def main():
    # The 'choice' variable controls the loop and contains the user's choice option.
    display_menu()
    
    # Get the user's choice option.
    choice = int(input("Choose option: "))
    
    # Perform the selected action.
    if choice == AREA_RECTANGLE_CHOICE:
        radius = float(input("Enter the radius of the circle: "))
        print("The area of rectangle is: ", circle.area(radius))
    elif choice == CIRCUMFERENCE_CHOICE:
        radius = float(input("Enter the radius of the circle: "))
        print("The length of the circle is: ", circle.circumference(radius))
    elif choice == AREA_RECTANGLE_CHOICE:
        width = float(input("Enter the width of the rectangle: "))
        length = float(input("Enter the length of the rectangle: "))
        print("The area of the rectangle is: ", rectangle.area(width,length))
    elif choice == PERIMETER_RECTANGLE_CHOICE:
        width = float(input("Enter the width of the rectangle: "))
        length = float(input("Enter the length of the rectangle: "))
        print("The perimeter of the rectangle is: ", rectangle.perimeter(width,length))
    elif choice == QUIT_CHOICE:
        print("Quit program.")
    else:
        print("Error. Invalid choice.")
        
# Function 'display_menu' shows menu.
def display_menu:
    print("Menu")
    print("1. Area of the circle")
    print("2. Length of the circle")
    print("3. Area of the rectangle")
    print("4. Perimeter of the rectangle")
    print("5. Quit")
    
# Call main function
main()

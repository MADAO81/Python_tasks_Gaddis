#This program demonstrates "remove" method

def main():
    # Create list with some values
    food = ["Pizza", "Burgers", "Chips", "Sushi", "Wok", "Burrito", "Tacos"]
    
    # Show the list
    print("Here is the list of food: ")
    print(food)
    
    # Get value that you want to replace
    item = input("What value should to delete?")
    
    try:
        # Delete Value
        food.remove(item)
        
        # show list
        print("Here is the changed list.")
        print(food)
        
    except ValueError: 
        print("This value not found in list.")
        
        
# Call main function
main()
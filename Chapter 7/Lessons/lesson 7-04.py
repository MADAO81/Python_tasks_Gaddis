#This program demonstrates how to get
# the index position of a value in a list and then
# replace that value with a new one.

def main():
    # Create list with some values
    food = ["Pizza", "Burgers", "Chips", "Sushi", "Wok", "Burrito", "Tacos"]
    
    # Show the list
    print("Here is the list of food: ")
    print(food)
    
    # Get value that you want to replace
    item = input("What value should to replace?")
    
    try:
        # Get index position in list
        item_index = food.index(item)
        
        # Get value to replace with
        new_item = input("Enter the new value: ")
        
        # Replace old value to new
        food[item_index] = new_item
        
        # Show the list
        print("Here is the changed list: ")
        print(food)
    except ValueError: 
        print("This value not found in list.")
        
# Call main function
main()
        
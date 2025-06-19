# task 10-05

# RetailItem class
from objects import retail # the class is stored in the objects folder

def main():
    # Создать три экземпляра класса RetailItem.
    item1 = retail.RetailItem("Jacket", 12, 59.95)
    item2 = retail.RetailItem("Designer Jeans", 40, 34.95)
    item3 = retail.RetailItem("Shirt", 20, 24.95) 
    
    # Show information 
    print("Item 1: ")
    print(item1)
    print()
    print("Item 2: ")
    print(item2)
    print()
    print("Item 3: ")
    print(item3)
    print()
    
# call main function 
main()
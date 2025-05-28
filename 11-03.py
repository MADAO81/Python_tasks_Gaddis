# task 11-03

# Person and Customer classes 

# import person 
from objects import person 

def main():
    name = ""
    address = ""
    phone_number = ""
    cust_number = 0 
    on_list_flag = False 
    
    # get data attributes 
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone_number = input("Enter the phone number: ")
    cust_number = input("Enter the customer ID: ")
    on_list = input("Does the client want to be on the mailing list? (Yes/No)")
    
    if on_list = "Yes":
        on_list_flag = True 
    else: 
        on_list_flag = False
        
    # create an instance of Customer class 
    customer = person.Customer(name, address, phone_number, cust_number, on_list_flag)
    
    # show info 
    print("Customer Information: ")
    print("Name: ", customer.get_name())
    print("Address: ", customer.get_address())
    print("Phone number: ", customer.get_phone_number())
    print("Customer ID: ", customer.get_cust_number())
    print("In mailing list:", customer.get_on_list())
    
# call main function 
main()
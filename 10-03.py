# task 10-03

# Personal data class "Information"

# import info 
from objects import info # the class is stored in the objects folder

def main():
    # Create three instances of the Information class
    my_info = info.Information("John Doe", "111 My street", 22, "555-555-1281")
    mom_info = info.Information("Mother", "222 Moms street", 52, "555-555-1234")
    sister_info = info.Information("Jane Doe", "333 Her street", 20, "555-555-4444")
    
    print("Information about me: ")
    display_info(my_info)
    print()
    print("Information about mother: ")
    display_info(mom_info)
    print()
    print("Information about sister: ")
    display_info(sister_info)
    
def display_info(info):
    print("Name: ", info.get_name())
    print("Address: ", info.get_address())
    print("Age: ", info.get_age())
    print("Phone number: ", info.get_phone_number())
    
# call main function
main()
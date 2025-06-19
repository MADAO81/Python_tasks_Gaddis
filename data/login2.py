# Analyzing the characters in the password
# Function get_login_name gets name, last name, ID as arguments.
# It returns login for enter the system

def get_login_name(first, last, idnumber):
    # Get 3 first letters of name. If name shorter, slice returns full name
    set1 = first[0:3]
    
    # Get 3 first letters of last name. If name shorter, slice returns full last name
    set2 = last[0:3]
    
    # Get 3 last numbers of id. If id shorter, slice returns full id 
    set3 = idnumber[-3:]
    
    # Assemble login 
    login_name = set1 + set2 + set3
    
    # return login to enter the system 
    return login_name 
    

# The valid_password function takes a password
# as an argument and returns true or false,
# indicating whether it is valid or invalid. A valid password must 
# consist of at least 7 characters, have at least one uppercase character, 
# one lowercase character, and one digit.    

def valid_password(password):
    # Set Boolean variables to False.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    # Begin validation
    if len(password) >= 7:
        correct_length = True 
        
        # analyze every symbol and set the appropriate flag when 
        # the required character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase = True 
            if ch.islower():
                has_lowercase = True 
            if ch.isdigit():
                has_digit = True 
                
        # Determine if all the requirements are met. If so, set is_valid to True. 
        # Otherwise, set is_valid to False.
        if correct_length and has_uppercase and has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False
            
        # return  valuable "is_valid"
        
        
        return is_valid 
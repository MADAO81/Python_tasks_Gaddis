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
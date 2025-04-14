# Write a function that takes a string value as an argument 
# and returns true if the argument ends with a substring ' .com'. 
# Otherwise, the function should return false.

def somefunction(somestring):
    if somestring[-4:-1] == ".com":
        return True 
        
# def somefunction(somestring):
#     if somestring.endswith(".com")
#         return True
#     else:
#         return False 
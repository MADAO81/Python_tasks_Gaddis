# The Ackerman function

def main():
    # test value 1 
    num1 = ackermann(0, 3)
    print(num1)
    
    # test value 2 
    num2 = ackermann(2, 0)
    print(num2)
    
    # test value 3
    num3 = ackermann(2, 3)
    print(num3)
    
# The Ackerman function is a recursive mathematical algorithm
# that is used to check how successfully the system optimizes its performance in the case of recursion.
def ackermann(m, n):
    if m == 0:
        return n + 1 
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n -1))
        
# call main function
main()
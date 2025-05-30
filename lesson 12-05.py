# This program uses recursion to print Fibonacci sequence numbers.

def main():
    print("First 10 numbers of Fibonacci sequence: ")
    
    for number in range(1, 11):
        print(fib(number))
        
# "fib" function returns n-number of Fibonacci sequence
def fib(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
# call main function
main()
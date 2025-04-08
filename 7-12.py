# Generating a prime number

def prime_or_composite(some_number):
    div = False
    for i in range(2, some_number):
        if some_number % i == 0:
            div = True
            
    if div:
        print(some_number, "is composite number.")
    else:
        print(some_number, "is simple number.")
        
def main():
    # get the number from user
    user_number = int(input("Enter your number: "))
    # create an empty list
    numbers = []
    
    for i in range(2, user_number +1):
        numbers.append(i)
        
    for number in range(len(numbers)):
        prime_or_composite(numbers[number])
        
# call main function
main()
    
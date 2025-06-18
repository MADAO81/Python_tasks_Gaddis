count = 0
user_value = 0
while count < 10:
    user_value = float(input("Enter the number: "))
    user_value +=user_value
    count +=1
print("Final sum is:", user_value)
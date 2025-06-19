# Write a loop that counts the number of digit characters in a string
# value referenced by mystring.

counter = 0
for ch in mystring:
    if ch.isdigit():
        counter +=1 
print("Number of digit characters:", counter)	
    
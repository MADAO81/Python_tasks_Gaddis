# Write a loop that counts the number of lowercase characters in a string
# value referenced by mystring.

counter = 0
for ch in mystring:
    if ch.islower():
        counter +=1 
print("Number of lowercase chars: ", counter)

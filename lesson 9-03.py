# This program demonstrates various operations on sets.
baseball = set({"Jody", "Carmen","Aida", "Alicia" })
basketball = set({"Eva", "Carmen", "Alicia", "Sarah"})

# Show members of the baseball set
print("These students are on the baseball team: ")
for name in baseball:
    print(name)
    
# Show members of the basketball set 
print("These students are on the basketball team: ")
for name in basketball:
    print(name)
    
# Demonstrate the intersection.
print()
print("These students are playing basketball and baseball both: ")
for name in baseball.intersection(basketball):
    print(name)
    
# Demonstrate unification.
print()
print("These students play one or both sports games: ")
for name in baseball.union(basketball):
    print(name)
    
# Demonstrate the difference between baseball and basketball.
print()
print("These students are playing baseball only: ")
for name in baseball.difference(basketball):
    print(name)
    
# Demonstrate the difference between basketbal and baseball.
print()
print("These students are playing basketball only: ")
for name in basketball.difference(baseball):
    print(name)
    
# Demonstrate the symmetrical difference
print()
print("These students play one of the sports games, but not both: ")
for name in baseball.symmetric_difference(basketball):
    print(name)
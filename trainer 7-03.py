import random

def main():
    list1 = []
    list2 = []
    for i in range(100):
        list1.append(random.randint(0,1000))
    
    list2 = list1.copy()
    print (list1)
    print (list2)
    
main()
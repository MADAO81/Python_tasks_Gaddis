# This program demonstrates the repetition operator.

def main():
    # print 9 lines, increasing by length
    for count in range(1, 10):
        print("z" * count)
        
    # print 9 lines, decreasing by length
    for count in range(8,0,-1):
        print("z" * count)
        
# call main function
main()
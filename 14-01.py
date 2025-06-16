# This program demonstrates
# a functional version of the factorial function

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value

def get_int(msg=''):
    return int(input(msg))

def main():
    # Pipeline (core with non-recursive factorial algorithm)ла)
    pipe(get_int('Enter a non-negative integer: '),    
         lambda n: (n, reduce(lambda x, y: x * y, range(1, n + 1))),    
         lambda tup: 
             print(f'The factorial of a number {tup[0]} equal to {tup[1]}'))        

# call main functi
main()
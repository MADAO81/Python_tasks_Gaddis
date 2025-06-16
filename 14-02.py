# This program demonstrates 
# # the functional version of the actual function

def pipe(data, *fseq):
    for fn in fseq: 
        data = fn(data)
    return data

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value

def get_int(msg=''):
    return int(input(msg))

def main():
    # Algorithm 1. Recursive version with tail recursion
    def factorial_rec(n): 
        fn = lambda n, acc=1: acc if n == 0 else fn(n - 1, acc * n)
        return n, fn(n) 
    
    # Algorithm 2. Non-recursive version
    def factorial(n):  
        return n, reduce(lambda x, y: x * y, range(1, n + 1)) 
    
    # data input 
    def indata():
        def validate(n):  # Validation of input data
            if not isinstance(n, int):
                raise TypeError("The number must be an integer.")
            if not n >= 0:
                raise ValueError("The number should be  >= 0.")
            return n        
        msg = 'Enter a non-negative integer: '
        return pipe(get_int(msg), validate)
    
    # data input 
    def outdata():
        def fn(data):
            n, fact = data
            print(f'factorial of number {n} equal {fact}') 
        return fn
 
    # Pipeline (functional core)
    pipe(indata(), factorial, outdata()) 
    
# call main function
main()
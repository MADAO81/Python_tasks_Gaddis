# This program demonstrates a functional version of the fibonacci function
def pipe(data, *fseq):
    for fn in fseq:
        data = fn(data)
    return data

def get_int(msg=''):
    return int(input(msg))

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value



def main():
    # Algorithm
    def fibonacci(n, x = 0, y = 1):
        # fib function returns the n-th number of the sequence
        fib = lambda n, x=0, y=1: x if n <= 0 else fib(n-1, y, x+y)
        # reduce function collects results to acc list
        acc = []
        reduce(lambda _, y: acc.append(fib(y)), range(n+1))
        return n, acc


    # Validation of input data
    def validate(n):
        if not isinstance(n, int):
            raise TypeError("The number must be an integer.")
        if not n >= 0:
            raise ValueError("The number must be zero or positive.")
        if n > 10:
            raise ValueError("The number should be no more than 10.")
        return n

    # data input
    def indata():
        msg = "Enter a non-negative integer no more than 10: "
        return pipe(get_int(msg), validate)

    # data output
    def outdata():
        def fn(data):
            n, seq = data
            msg = f" First {n} Fibonacci sequence numbers:"
            print(msg)
            [print(el) for el in seq]
        return fn

    # Pipeline (functional core)
    pipe(indata(), fibonacci, outdata())

# call main function
main()